import contextlib
import os
import shutil
import subprocess
import sys

from pathlib import Path

from invoke import task


WINDOWS = sys.platform.startswith("win")
ROOT_DIR = Path(__file__).parent
BIN_DIR = Path(sys.executable).parent
OUTPUT_DIR = ROOT_DIR / "output"
SERVE_PORT = 8000
SSH_CONFIG = ROOT_DIR / "private" / "ssh.config"
DEPLOY_PATH = "/var/www/html/main/"


@task
def build(ctx):
    """Build the site."""
    ctx.run(
        f'{BIN_DIR / "pelican"} --fatal warnings ' f'-s {ROOT_DIR / "pelicanconf.py"}',
        pty=True,  # Hangs w/o this with the search plugin.
    )


@task
def clean(_ctx):
    """Clean the build output."""
    with contextlib.suppress(FileNotFoundError):
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir()


@task
def serve(ctx):
    """Start a web server to serve up the site (blocks)."""
    print("Serving on http://localhost:", SERVE_PORT, sep="")
    ctx.run(f'{BIN_DIR / "pelican"} --listen --port {SERVE_PORT}')


@task
def watch(ctx):
    """Serve the site and rebuild when changes are detected (blocks)."""
    ctx.run(
        f'{BIN_DIR / "pelican"} '
        f'-s {ROOT_DIR / "pelicanconf.py"} --autoreload '
        f'--listen --port {SERVE_PORT}',
        pty=True,
    )


@task
def deploy(ctx):
    """Deploy latest build to production."""
    print("Copying files...")
    source = str(OUTPUT_DIR) + "/*"
    if WINDOWS:
        ctx.run(f'scp -F "{SSH_CONFIG}" -r "{source}" web:{DEPLOY_PATH}')
    else:
        ctx.run(
            "rsync --delete --stats -pthrzv -c "
            f'-e "ssh -F {SSH_CONFIG} -oStrictHostKeyChecking=no" '
            f"{source} web:{DEPLOY_PATH}"
        )


@task(help={"host": "Host from ssh.config to which to connect."})
def ssh(_ctx, host="web"):
    """ssh into the blog's host."""
    user_ssh_dir = Path.home() / ".ssh"  # Ensure .ssh dir exists.
    user_ssh_dir.mkdir(mode=0o700, exist_ok=True)
    with chdir(ROOT_DIR):
        command = ["ssh", "-F", f"{SSH_CONFIG}", f"{host}"]
        print(" ".join(command))
        subprocess.run(command)


@contextlib.contextmanager
def chdir(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)

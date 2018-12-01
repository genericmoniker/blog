import contextlib
import os
import shutil
import subprocess
import sys

from pathlib import Path

from invoke import task


WINDOWS = sys.platform.startswith('win')
ROOT_DIR = Path(__file__).parent
BIN_DIR = Path(sys.executable).parent
THEME_DIR = ROOT_DIR / 'theme'
OUTPUT_DIR = ROOT_DIR / 'output'
SERVE_PORT = 8000
SSH_CONFIG = ROOT_DIR / 'private' / 'ssh.config'
SSH_KEY = ROOT_DIR / 'private' / 'id_rsa'
DEPLOY_PATH = '/var/www/html/main/'


@task
def requirements(ctx):
    """Update requirements*.txt from requirements*.in."""
    in_files = ROOT_DIR.glob('requirements*.in')
    for in_file in in_files:
        ctx.run(f'{BIN_DIR / "pip-compile"} {in_file}')


@task
def build_content(ctx):
    """Build the site content."""
    ctx.run(
        f'{BIN_DIR / "pelican"} --fatal warnings '
        f'-s {ROOT_DIR / "pelicanconf.py"}'
    )


@task
def build_theme(ctx):
    """Build the site theme."""
    scss_file = ROOT_DIR / 'theme' / 'scss' / 'main.scss'
    scss_mtime = os.stat(scss_file).st_mtime
    css_file = ROOT_DIR / 'theme' / 'static' / 'css' / 'main.css'
    css_mtime = os.stat(css_file).st_mtime
    if scss_mtime >= css_mtime:
        ctx.run(f'{BIN_DIR / "pysassc"} --sourcemap {scss_file} {css_file}')


@task(pre=[build_theme, build_content])
def build(_ctx):
    """Build everything."""


@task
def clean(_ctx):
    """Clean the build output."""
    shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.makedir()


@task
def serve(ctx):
    """Start a web server to serve up the site (blocks)."""
    print('Serving on http://localhost:', SERVE_PORT)
    ctx.run(f'{BIN_DIR / "pelican"} --listen --port {SERVE_PORT}')


@task
def deploy(ctx):
    """Deploy latest build to production."""
    print('Copying files...')
    source = str(OUTPUT_DIR) + '/.'
    if WINDOWS:
        ctx.run(f'scp -F "{SSH_CONFIG}" -r "{source}" web:{DEPLOY_PATH}')
    else:
        ctx.run(
            'rsync --delete --stats -pthrz -c '
            f'-e "ssh -F {SSH_CONFIG}" '  # Explicit ssh to use config file.
            f'{source} web:{DEPLOY_PATH}'
        )


@task(help={'host': 'Host from ssh.config to which to connect.'})
def ssh(_ctx, host='web'):
    """ssh into the blog's host."""
    user_ssh_dir = Path.home() / '.ssh'  # Ensure .ssh dir exists.
    user_ssh_dir.mkdir(mode=0o700, exist_ok=True)
    with chdir(ROOT_DIR):
        command = ['ssh', '-F', f'{SSH_CONFIG}', f'{host}']
        print(' '.join(command))
        subprocess.run(command)


@contextlib.contextmanager
def chdir(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)

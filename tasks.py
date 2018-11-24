import os
import shutil
import subprocess
import sys

from pathlib import Path

from invoke import task


WINDOWS = sys.platform.startswith('win')
ROOT_DIR = Path(__file__).parent
BIN_DIR = ROOT_DIR / '.venv' / 'Scripts' if WINDOWS else 'bin'
THEME_DIR = ROOT_DIR / 'theme'
OUTPUT_DIR = ROOT_DIR / 'output'
SERVE_PORT = 8000
SSH_CONFIG = ROOT_DIR / 'private' / 'ssh.config'
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


@task(pre=[build])
def deploy(ctx):
    """Deploy to production."""
    print('Copying files...')
    source = str(OUTPUT_DIR) + '/.'
    if WINDOWS:
        ctx.run(f'scp -F "{SSH_CONFIG}" -r "{source}" web:{DEPLOY_PATH}')
    else:
        ctx.run(
            f'rsync -F "{SSH_CONFIG}" --delete -pthrvz -c '
            f'{source} web:{DEPLOY_PATH}'
        )


@task(help={'host': 'Host from ssh.config to which to connect.'})
def ssh(_ctx, host='web'):
    """ssh into the blog's host."""
    config = SSH_CONFIG
    subprocess.run(f'ssh -F {config} {host}')

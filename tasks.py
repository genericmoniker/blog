import os
import shutil
import socketserver

import sys
from fnmatch import fnmatch

import time
from invoke import task
from pelican import read_settings
from pelican.readers import MarkdownReader

from pelican.server import ComplexHTTPRequestHandler

# Note: invoke.yaml needed to work around a problem with invoke on Windows:
# https://github.com/pyinvoke/invoke/issues/345

SOURCE_DIR = os.path.abspath(os.path.dirname(__file__))
SETTINGS = os.path.join(SOURCE_DIR, 'pelicanconf.py')
CONTENT_DIR = os.path.join(SOURCE_DIR, 'content')
THEME_DIR = os.path.join(SOURCE_DIR, 'theme')
OUTPUT_DIR = os.path.join(SOURCE_DIR, 'output')
INDEX = os.path.join(OUTPUT_DIR, '_search_index_')
SITE = os.path.join(OUTPUT_DIR, '_search_index_')
SERVE_PORT = 8000


@task
def requirements(ctx):
    """Update requirements.txt from requirements.in."""
    try:
        os.remove(os.path.join(SOURCE_DIR, 'requirements.txt'))
    except FileNotFoundError:
        pass
    ctx.run('pip-compile requirements.in')


@task(name='requirements-dev')
def requirements_dev(ctx):
    """Update requirements_dev.txt from requirements_dev.in."""
    try:
        os.remove(os.path.join(SOURCE_DIR, 'requirements_dev.txt'))
    except FileNotFoundError:
        pass
    ctx.run('pip-compile requirements_dev.in')


@task(name='build-content')
def build_content(ctx):
    """Build the blog content."""
    ctx.run('pelican -s pelicanconf.py')


@task(name='build-theme')
def build_theme(ctx):
    """Build the site theme."""
    scss_file = os.path.join(THEME_DIR, 'scss', 'main.scss')
    scss_mtime = os.stat(scss_file).st_mtime
    css_file = os.path.join(THEME_DIR, 'static', 'css', 'main.css')
    css_mtime = os.stat(css_file).st_mtime
    if scss_mtime >= css_mtime:
        ctx.run(f'sassc --sourcemap {scss_file} {css_file}')


@task
def index(ctx):
    """Build the search index."""
    from whoosh.fields import Schema
    from whoosh.fields import TEXT
    from whoosh.fields import ID
    from whoosh.index import create_in

    start = time.time()
    os.makedirs(INDEX, exist_ok=True)

    schema = Schema(
        title=TEXT(stored=True),
        path=ID(stored=True),
        content=TEXT)
    ix = create_in(INDEX, schema)
    writer = ix.writer()
    for root, dirs, names in os.walk(CONTENT_DIR):
        for name in names:
            if fnmatch(name, '*.md'):
                path = os.path.join(root, name)
                writer.add_document(**extract_document(path))
    writer.commit()
    end = time.time() - start
    print('Indexed {} documents ({:.2f} s)'.format(ix.doc_count(), end))


def extract_document(path):
    from pelicanconf import ARTICLE_URL

    # The MarkdownReader gives the HTML and metadata, but I'm thinking the
    # raw markdown will index better, so just using the metadata here.
    _, metadata = MarkdownReader(read_settings(SETTINGS)).read(path)
    url = ARTICLE_URL.format(**metadata)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    return dict(
        title=metadata['title'],
        path=url,
        content=content)


@task(pre=[build_theme, build_content])
def build(ctx):
    """Build everything."""


@task
def clean(ctx):
    """Clean the build output."""
    shutil.rmtree(OUTPUT_DIR)


@task
def serve(ctx):
    """Start a web server to serve up the site (blocks)."""
    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    os.chdir(OUTPUT_DIR)
    server = AddressReuseTCPServer(('', SERVE_PORT), ComplexHTTPRequestHandler)
    sys.stderr.write('Serving on port {0} ...\n'.format(SERVE_PORT))
    server.serve_forever()

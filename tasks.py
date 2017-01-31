# -*- coding: utf-8 -*-
import os
import socketserver

import sys
from invoke import task

from pelican.server import ComplexHTTPRequestHandler

# Major hack. https://github.com/pyinvoke/invoke/issues/345
CMD = r'C:\Windows\system32\cmd.EXE'

OUTPUT = 'output'
SERVE_PORT = 8000


@task
def build(ctx):
    """Build the web site."""
    ctx.run('pelican -D -s pelicanconf.py', color=True, shell=CMD)


@task
def serve(ctx):
    """Start a web server to serve up the site."""
    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    os.chdir(OUTPUT)
    server = AddressReuseTCPServer(('', SERVE_PORT), ComplexHTTPRequestHandler)
    sys.stderr.write('Serving on port {0} ...\n'.format(SERVE_PORT))
    server.serve_forever()

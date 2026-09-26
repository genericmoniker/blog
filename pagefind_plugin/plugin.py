"""Simple Pelican plugin to build the Pagefind search index for the site.

This is done as a plugin so that any Pelican build (including with autoreload) will also
build the Pagefind index.
"""

import subprocess
import sys

from pathlib import Path

from pelican import signals


def _build_pagefind_index(pelican):
    output_path = Path(str(pelican.settings.get("OUTPUT_PATH", "output")))
    command = [sys.executable, "-m", "pagefind", "--site", str(output_path)]

    subprocess.run(command, check=True)


def register():
    signals.finalized.connect(_build_pagefind_index)

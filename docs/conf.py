"""Sphinx configuration."""

from datetime import datetime

project = "Hypermodern Python for ML Cookiecutter"
author = "Matthew Sach"
copyright = f"{datetime.now().year}, {author}"
extensions = ["myst-parser"]
language = "en"
html_theme = "furo"
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
]

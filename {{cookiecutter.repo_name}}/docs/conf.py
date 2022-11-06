"""Sphinx configuration."""
project = "{{cookiecutter.project_name}}"
author = "{{cookiecutter.author_name}}"
copyright = "{{cookiecutter.copyright_year}}, {{cookiecutter.author_name}}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "myst_parser"]
autodoc_typehints = "description"
html_theme = "furo"

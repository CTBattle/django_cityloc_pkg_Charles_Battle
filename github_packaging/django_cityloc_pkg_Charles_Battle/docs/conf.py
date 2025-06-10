# docs/conf.py
import os, sys
sys.path.insert(0, os.path.abspath('..'))   # lets autodoc find your package

project   = 'django_cityloc_pkg'
author    = 'Charles Battle'
release   = '0.0.1'

extensions       = ['sphinx.ext.autodoc']    # enables docstring support
templates_path   = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme       = 'alabaster'
html_static_path = ['_static']
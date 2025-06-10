# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#    Path setup

import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # so autodoc can find your package


#  Project information 

project = 'django_cityloc_pkg'
copyright = '2023, Charles Battle'
author = 'Charles Battle'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


#    General configuration 


extensions = [
    'sphinx.ext.autodoc',          # auto-generate docs from docstrings
    'sphinx.ext.napoleon',         # support Google/NumPy style docstrings
    'sphinx.ext.todo',             # support todo directives
    'sphinx.ext.intersphinx'       # link to other projects' docs (e.g., Python stdlib)
]

# Include TODOs in the built docs
todo_include_todos = True

# Templates path
templates_path = ['_templates']

# Patterns to exclude
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Language setting
language = 'en'

# Show function/class members in order of appearance in source
autodoc_member_order = 'bysource'

# Intersphinx mapping to Python docs
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}


#    Options for HTML output 

html_theme = 'alabaster'
html_static_path = ['_static']

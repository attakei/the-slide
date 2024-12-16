# Configuration file for the Sphinx documentation builder.
# -- Project information
project = "the-slide"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = "0.0.0"

# -- General configuration
extensions = [
    "sphinx_revealjs",
    "the_slide",
]
templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]

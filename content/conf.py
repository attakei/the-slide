# Configuration file for the Sphinx documentation builder.
# -- Project information
project = "the-slide"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = "1.0.1"

# -- General configuration
extensions = [
    # Bundiled extensions
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    # My extensions
    "oembedpy.adapters.sphinx",
    "sphinx_revealjs",
    # Third-party extensions
    "pyvista.ext.plot_directive",
    "pyvista.ext.viewer_directive",
    "sphinx_design",
    "sphinx_nekochan",
    "sphinx_plotly_directive",
    "sphinxcontrib.asciinema",
    "sphinxcontrib.mermaid",
    "sphinxemoji.sphinxemoji",
    # Itself
    "the_slide",
]
templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for REVEALJS output
revealjs_style_theme = "css/theme.css"
revealjs_static_path = ["_static"]
revealjs_css_files = []
revealjs_script_conf = {
    "controls": False,
    "hash": True,
    "center": False,
    "transition": "none",
}
revealjs_script_plugins = [
    {
        "src": "revealjs/plugin/highlight/highlight.js",
        "name": "RevealHighlight",
    },
    {
        "src": "revealjs/plugin/notes/notes.js",
        "name": "RevealNotes",
    },
]
pygments_style = "monokai"
# -- Options for extensions
# sphinxcontrib.mermaid
mermaid_version = "11.4.1"
mermaid_output_format = "svg"
mermaid_cmd = "pnpm mmdc -p puppeteer-config.json"


def setup(app) -> dict:
    print("Working this extension!")

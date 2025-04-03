# Configuration file for the Sphinx documentation builder.
import os

# -- Project information
project = "the-slide"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = "1.0.3"

# -- General configuration
extensions = [
    # Bundled extensions
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    # My extensions
    "oembedpy.adapters.sphinx",
    "sphinx_revealjs",
    "sphinx_revealjs.ext.oembed",
    "sphinx_revealjs.ext.screenshot",
    # Third-party extensions
    "pyvista.ext.plot_directive",
    "pyvista.ext.viewer_directive",
    "sphinx_design",
    "sphinx_nekochan",
    "sphinx_plotly_directive",
    "sphinxcontrib.asciinema",
    "sphinxcontrib.mermaid",
    "sphinxemoji.sphinxemoji",
    "sphinxext.opengraph",
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
    "width": 1280,
    "height": 720,
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
# sphinxext.opengraph
ogp_site_url = os.environ.get("SITE_URLBASE", "http://localhost:8000/")
ogp_type = "article"
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image" >',
    '<meta name="twitter:site" content="@attakei" >',
]
ogp_enable_meta_description = True
# sphinx_revealjs.ext.oembed
revealjs_oembed_urlbase = ogp_site_url[:-1]

from docutils import nodes
from sphinx_revealjs.nodes import revealjs_vertical, revealjs_section


def configure_background(app, doctree, docname):
    for section in doctree.traverse(nodes.section):
        if isinstance(section.parent, nodes.document):
            continue
        if not isinstance(section.parent.parent, nodes.document):
            continue
        idx = section.first_child_matching_class(revealjs_section)
        if idx is None:
            s = revealjs_section()
            s.attributes["data-background-image"] = "_static/background/2.png"
            s.attributes["data-background-size"] = "auto"
            section.insert(1, s)
        idx = section.first_child_matching_class(revealjs_vertical)
        if idx is None:
            s = revealjs_vertical()
            s.attributes["data-background-image"] = "_static/background/4.png"
            s.attributes["data-background-size"] = "auto"
            section.insert(1, s)


def setup(app):
    app.connect("doctree-resolved", configure_background)
    return {}


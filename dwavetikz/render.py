from jinja2 import Environment, PackageLoader


def render(template_name, **kwargs):
    environment = Environment(loader=PackageLoader("dwavetikz", "templates"))
    template = environment.get_template(template_name)
    return template.render(**kwargs)

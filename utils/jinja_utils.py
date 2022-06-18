from jinja2 import PackageLoader, Environment


def create_environment(templates_location: str):
    return Environment(loader=PackageLoader(templates_location))

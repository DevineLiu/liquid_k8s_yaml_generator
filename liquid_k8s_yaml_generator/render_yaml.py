from jinja2 import Environment, FileSystemLoader
from os.path import dirname, join, abspath

_default_path = join(dirname(abspath(__file__)), 'templates')

env = Environment(
    loader=FileSystemLoader(_default_path), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("test_tpl.tmpl")


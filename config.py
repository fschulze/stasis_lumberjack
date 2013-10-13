from jinja2 import Environment, FileSystemLoader
from stasis import Configurator
from stasis.node import Node
import yaml
import os


def config_factory(registry):
    with open(os.path.join(registry['path'], 'lumberjack.yml')) as config:
        return yaml.load(config.read())


def jinja_env(request):
    if 'jinja_env' not in request.registry:
        request.registry['jinja_env'] = Environment(
            loader=FileSystemLoader([
                os.path.join(request.registry['path'], 'templates'),
                request.registry['root'].abspath]))
    return request.registry['jinja_env']


config = Configurator()
config.add_node_factory('.html', '__main__.views.Page')
config.set_config_factory(config_factory)
config.set_root_factory(Node(config.registry, root='content'))
config.add_request_method(jinja_env)
config.scan('__main__.views')

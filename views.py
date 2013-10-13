from pyramid.response import FileResponse
from pyramid.view import view_config
from stasis.node import Node


class Page(Node):
    pass


@view_config(context=Page, renderer='string')
def page_view(context, request):
    template = request.jinja_env().get_template(context.path)
    result = template.render(request.registry['siteconfig']['site'])
    return result


@view_config(context=Node)
def node_view(context, request):
    return FileResponse(context.abspath, request)

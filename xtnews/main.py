# coding: utf-8

import types
import logging
import argparse
import collections
from webob import Response
from webob.dec import wsgify
from webob.exc import HTTPBadRequest, HTTPNotFound, HTTPMethodNotAllowed
from wsgiref.simple_server import make_server
from wsgiref.validate import validator
from xtnews import storage

logger = logging.getLogger(__name__)

OBJECT_METHOD_MAP = {
    'GET': 'get',
    'POST': 'add',
    'PUT': 'update',
    'DELETE': 'delete',
}

OBJECT_TEMPLATE = """<object id="%(id)s" subject="%(subject)s" dateCreated="%(date_created)s">%(text)s</object>"""

class Application(object):

    def render_form_response(self, item, errors):
        yield "<form>"
        yield self.render_item(item)
        if errors:
            yield "<errors>"
            for field_name, error_text in errors.items():
                yield '<error field="%s">%s</error>' % (field_name, error_text)
            yield "</errors>"

        yield "</form>"

    def render_item(self, data):
        return str(OBJECT_TEMPLATE % data)

    def render_list(self, data):
        yield "<objects>"
        for item in data:
            yield self.render_item(item)
        yield "</objects>"

    def make_response(self, data):
        if not isinstance(data, (list, tuple, types.GeneratorType)):
            data = [data]
        return Response(app_iter=data, headerlist=[('Content-type', 'text/xml')])

    def get_object_id(self, path):
        object_id = path[1:]
        if not object_id:
            return None
        if object_id.endswith('/'):
            object_id = object_id[:-1]
        try:
            object_id = int(object_id)
        except Exception, e:
            raise HTTPBadRequest(e)

        return object_id

    @wsgify
    def __call__(self, request):
        object_id = self.get_object_id(request.path)

        if not object_id and request.method == 'GET':
            return self.make_response(self.render_list(storage.all()))

        try:
            method_name = OBJECT_METHOD_MAP.get(request.method)
        except KeyError:
            raise HTTPMethodNotAllowed(request.method)

        try:
            method = getattr(storage, method_name)
        except AttributeError, e:
            raise HTTPBadRequest(e)

        params = getattr(request, request.method, {})

        try:
            return self.make_response(self.render_item(method(object_id, params)))
        except storage.ValidationError, e:
            return self.make_response(self.render_form_response(e.item, e.errors))
        except IndexError, e:
            raise HTTPNotFound("Object with id %s not found" % object_id)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', default='')
    parser.add_argument('-p', '--port', type=int, default=5000)
    return parser.parse_args()

def run():
    args = get_args()
    logging.basicConfig(level=logging.INFO)
    app = validator(Application())
    httpd = make_server(args.host, args.port, app)
    logger.info('Starting application on %s:%s', args.host or '0.0.0.0', args.port)
    httpd.serve_forever()


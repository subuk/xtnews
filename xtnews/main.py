# coding: utf-8

import types
import logging
import argparse
import collections
from webob import Response
from webob.dec import wsgify
from webob.exc import HTTPBadRequest, HTTPNotFound
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

OBJECT_TEMPLATE = """\
<object id="%(id)s" subject="%(subject)s" date_created="%(date_created)s">%(text)s</object>
"""

class Application(object):
    allowed_methods = ('GET', 'POST')

    def render_item(self, data):
        return OBJECT_TEMPLATE % data

    def render_list(self, data):
        yield "<objects>"
        for item in data:
            yield self.render_item(item)
        yield "</objects>"

    def respond(self, data):
        if not isinstance(data, (list, tuple, types.GeneratorType)):
            data = [data]
        return Response(app_iter=data, headerlist=[('Content-type', 'text/xml')])

    def get_object_id(self, path):
        object_id = path[1:]
        if object_id:
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
            return self.respond(self.render_list(storage.all()))

        method_name = OBJECT_METHOD_MAP.get(request.method)

        try:
            method = getattr(storage, method_name)
        except AttributeError, e:
            raise HTTPBadRequest(e)

        params = getattr(request, request.method, {})
        try:
            return self.respond(self.render_item(method(object_id, **params)))
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


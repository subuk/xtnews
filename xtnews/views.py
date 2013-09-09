
import transaction
from pyramid.view import view_config
from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPNoContent, HTTPCreated
from forms import NewsForm
from xtnews import models

class BaseView(object):

    def __init__(self, request):
        self.request = request
        self.request.response.content_type = 'application/xml'


class Collection(BaseView):

    def get_object_list(self):
        return models.DBSession.query(models.News).all()

    @view_config(route_name='list', renderer='object_list.xml.jinja2', request_method='GET')
    def get(self):
        return {
            'object_list': ( x.as_dict() for x in self.get_object_list())
        }

    @view_config(route_name='list', renderer='object_form_errors.xml.jinja2', request_method='POST')
    def post(self):
        form = NewsForm(**self.request.POST)
        if not form.validate():
            self.request.response.status = 400
            return {'form': form}
        obj = models.News()
        form.populate_obj(obj)
        models.DBSession.add(obj)
        transaction.commit()
        return HTTPCreated()

class Item(BaseView):

    def get_object(self, object_id):
        obj = models.DBSession.query(models.News).get(object_id)
        if not obj:
            raise NotFound("Object with id %s not found" % object_id)
        return obj

    @view_config(route_name='item', renderer='object.xml.jinja2', request_method='GET')
    def get(self):
        obj = self.get_object(self.request.matchdict['id'])
        return {
            'object': obj.as_dict(),
        }

    @view_config(route_name='item', renderer='object.xml.jinja2', request_method='DELETE')
    def delete(self):
        obj = self.get_object(self.request.matchdict['id'])
        models.DBSession.delete(obj)
        return HTTPNoContent()

    @view_config(route_name='item', renderer='object_form_errors.xml.jinja2', request_method='PUT')
    def put(self):
        form = NewsForm(**self.request.POST)
        if not form.validate():
            self.request.response.status = 400
            return {'form': form}
        obj = self.get_object(self.request.matchdict['id'])
        form.populate_obj(obj)
        models.DBSession.add(obj)
        transaction.commit()
        return HTTPNoContent()

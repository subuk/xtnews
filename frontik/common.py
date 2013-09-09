
import frontik.handler
from tornado.web import HTTPError

def xsl(xsl_name):
    def __dec(func):
        def __func(self, *args, **kwargs):
            self.set_xsl(xsl_name)
            func(self, *args, **kwargs)
        return __func
    return __dec

class PageHandler(frontik.handler.PageHandler):

    def on_object_fetched(self, data, response):
        if response.error:
            raise HTTPError(response.code)
        self.doc.put(data)

    def on_object_deleted(self, data, response):
        raise NotImplementedError()

    def get_object_url(self, object_id):
        return "%s%s" % (self.config.app_base_url, object_id)

    def delete_object(self, object_id):
        self.delete_url(self.get_object_url(object_id), callback=self.on_object_deleted)

    def fetch_object(self, object_id):
        self.get_url(self.get_object_url(object_id), callback=self.on_object_fetched)

    def fetch_object_list(self):
        self.doc.put(self.get_url(self.config.app_base_url))


import frontik.handler
from frontik.doc import Doc

frontik_import("common")

class Page(common.PageHandler):

    @common.xsl('index.xsl')
    def get_page(self):
        self.fetch_object_list()

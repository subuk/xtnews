
import frontik.handler

frontik_import("common")

class Page(common.PageHandler):

    @common.xsl('index.xsl')
    def get_page(self):
        object_id = self.get_argument('id')
        self.fetch_object(object_id)




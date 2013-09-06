
import frontik.handler
from frontik.doc import Doc

class Page(frontik.handler.PageHandler):
    def get_page(self):
        self.set_xsl('index.xsl')
        self.doc.put(self.get_url(self.config.app_base_url))

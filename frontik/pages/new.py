
import logging
import frontik.handler

logger = logging.getLogger(__name__)

class Page(frontik.handler.PageHandler):

    def get_page(self):
        self.set_xsl('new.xsl')
        self.finish_page()

    def post_page(self):
        self.set_xsl('new.xsl')
        self.doc.put(self.post_url(self.config.app_base_url, data=self.request.body))





import logging
from lxml import etree
import frontik.handler
from frontik.doc import Doc

logger = logging.getLogger(__name__)

FORM_XML = etree.fromstring("""\
<form />
""")

class Page(frontik.handler.PageHandler):
    def get_page(self):
        self.set_xsl('index.xsl')
        self.doc.put(FORM_XML)

    def on_response(self, data, response):
        if response.code == 400:
            data = etree.fromstring(response.body)
            return self.doc.put(data)
        self.redirect('../')

    def post_page(self):
        self.set_xsl('index.xsl')
        self.post_url(self.config.app_base_url, data=self.request.body, callback=self.on_response)

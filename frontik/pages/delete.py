
import frontik.handler
from lxml import etree

FORM_XML = etree.fromstring("""\
<deleteConfirmation />
""")

frontik_import("common")

class Page(common.PageHandler):

    @common.xsl('index.xsl')
    def get_page(self):
        self.fetch_object(self.get_argument('id'))
        self.doc.put(FORM_XML)

    def on_object_deleted(self, data, response):
        return self.redirect('../../')

    def post_page(self):
        return self.delete_object(self.get_argument('id'))


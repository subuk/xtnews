
import logging
import frontik.handler
from frontik.doc import Doc
from lxml import etree

logger = logging.getLogger(__name__)

FORM_XML = etree.fromstring("""\
<?xml version="1.0" encoding="utf-8"?>
<form>
    <fields>
        <field tagName="input" name="subject" value="Subject example">
            <error>hello</error>
        </field>
        <field tagName="textarea" name="text" value="Subject example">
            <error>hello</error>
        </field>
    </fields>
    <errors>
        <error fieldName="subject">This field is required</error>
    </errors>
</form>
""")

class Page(frontik.handler.PageHandler):
    def get_page(self):
        self.set_xsl('index.xsl')
        self.doc.put(FORM_XML)

    def post_page(self):
        self.set_xsl('new.xsl')
        self.doc.put(self.post_url(self.config.app_base_url, data=self.request.body))

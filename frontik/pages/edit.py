
from lxml import etree

import frontik.handler

frontik_import("common")

FORM_XML = etree.fromstring("""\
<form />
""")


class Page(common.PageHandler):

    @common.xsl('index.xsl')
    def get_page(self):
        object_id = self.get_argument('id')
        self.doc.put(FORM_XML)
        self.fetch_object(object_id)

    def on_response(self, data, response):
        if response.code == 400:
            data = etree.fromstring(response.body)
            return self.doc.put(data)
        self.redirect('../')

    @common.xsl('index.xsl')
    def post_page(self):
        object_id = self.get_argument('id')
        self.put_url(self.get_object_url(object_id),
            data=self.request.body,
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            callback=self.on_response)

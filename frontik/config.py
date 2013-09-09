
import os

XSL_root = os.path.normpath(os.path.join(os.path.dirname(__file__), "./xsl"))
XML_root = os.path.normpath(os.path.join(os.path.dirname(__file__), "./xml" ))

# Trailing slash required
app_base_url = "http://127.0.0.1:6543/"

version = '0.1'

apply_xsl = True

frontik_import("pages")
frontik_import("pages.detail")
frontik_import("pages.delete")
frontik_import("pages.edit")

from frontik.app import Map2ModuleName

urls = [
    ("^(?P<id>\d+)/delete/$", pages.delete.Page),
    ("^(?P<id>\d+)/edit/$", pages.edit.Page),
    ("^(?P<id>\d+)/$", pages.detail.Page),

    ("", Map2ModuleName(pages)),



]

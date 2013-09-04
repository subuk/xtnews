
import os

XSL_root = os.path.normpath(os.path.join(os.path.dirname(__file__), "./xsl"))
XML_root = os.path.normpath(os.path.join(os.path.dirname(__file__), "./xml" ))

# Trailing slash required
app_base_url = "http://127.0.0.1:5000/"

version = '0.1'

apply_xsl = True



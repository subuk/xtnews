<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="html"
  encoding="UTF-8"
  indent="yes"
  cdata-section-elements="script noscript"
  undeclare-namespaces="yes"
  omit-xml-declaration="yes"
  doctype-system="about:legacy-compat"/>

<xsl:include href="chunks/object.xsl"/>

<xsl:template match="/">
    <xsl:for-each select="//objects/object">
        <xsl:call-template name="object" />
    </xsl:for-each>
    <a href="new/">Add</a>
</xsl:template>

</xsl:stylesheet>

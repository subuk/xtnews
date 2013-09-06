<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="html"
  encoding="UTF-8"
  indent="yes"
  cdata-section-elements="script noscript"
  undeclare-namespaces="yes"
  omit-xml-declaration="yes"
  doctype-system="about:legacy-compat" />

<xsl:include href="chunks/formatdate.xsl" />

<xsl:template match="object">
  <div class="media">
    <div class="media-body">
      <h4 class="media-heading"><xsl:value-of select="@subject"/></h4>
      <p><xsl:value-of select="."/></p>
      <p>
        <xsl:call-template name="FormatDate">
          <xsl:with-param name="DateTime" select="@dateCreated"/>
        </xsl:call-template>
      </p>
    </div>
  </div>
</xsl:template>

<xsl:template match="fields">
  <xsl:variable name="fieldTag" select="field/@tagName" />

  <xsl:if test="{$fieldTag} == textarea ">

  </xsl:if>

  <xsl:element name="{$fieldTag}">
    <xsl:attribute name="name">
      <xsl:value-of select="field/@name" />
    </xsl:attribute>
  </xsl:element>

  <xsl:if test="field/error/text()">
    <p><xsl:value-of select="field/error/text()" /></p>
  </xsl:if>

</xsl:template>

</xsl:stylesheet>



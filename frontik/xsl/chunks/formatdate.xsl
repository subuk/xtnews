<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<xsl:template name="FormatDate">
  <xsl:param name="DateTime" />
  <xsl:variable name="date">
    <xsl:value-of select="substring-before($DateTime,'T')" />
  </xsl:variable>

  <xsl:if test="string-length($date) != 10">
    <xsl:value-of select="$DateTime"/>
  </xsl:if>
  <xsl:if test="string-length($date) = 10">
    <xsl:value-of select="$date"/>
  </xsl:if>
</xsl:template>

</xsl:stylesheet>

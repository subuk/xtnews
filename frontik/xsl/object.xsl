<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template name="object">
  <div class="media">
    <div class="media-body">
      <h4 class="media-heading"><xsl:value-of select="@subject"/></h4>
      <p><xsl:value-of select="."/></p>
      <p><xsl:value-of select="@date_created"/></p>
    </div>
  </div>
</xsl:template>

</xsl:stylesheet>

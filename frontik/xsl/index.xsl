<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
    <xsl:for-each select="//objects/object">
        <div class="media">

          <div class="media-body">
            <h4 class="media-heading">Media heading</h4>
                <xsl:value-of select="@subject"/>
                <xsl:value-of select="text"/>
                <p><xsl:value-of select="@date_created"/></p>
          </div>
        </div>
    </xsl:for-each>
</xsl:template>


</xsl:stylesheet>

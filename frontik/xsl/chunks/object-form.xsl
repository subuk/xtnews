<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template name="object-form">

  <xsl:variable name="subject-error">
    <xsl:value-of select="//formResponse/errors/error[contains(@field, 'subject')]" />
  </xsl:variable>

  <xsl:variable name="text-error">
    <xsl:value-of select="//formResponse/errors/error[contains(@field, 'subject')]" />
  </xsl:variable>

  <form role="form" method="post" action="">
    <div class="form-group">
      <label for="subject">Subject</label>
      <input type="text" class="form-control" id="subject" name="subject" placeholder="Text">
        <!-- <xsl:attribute name="value">
          <xsl:value-of select="//formResponse/errors/error[contains(@field, 'subject')]" />
        </xsl:attribute> -->
      </input>
      <xsl:if test="//formResponse/errors/error[contains(@field, 'subject')]">
        <p>
          <xsl:value-of select="//formResponse/errors/error[contains(@field, 'subject')]" />
        </p>
      </xsl:if>
    </div>

    <div class="form-group">
      <label for="text">Text</label>
      <textarea id="text" name="text">
        <!-- <xsl:value-of select="//formResponse/errors/error[contains(@field, 'text')]" /> -->
      </textarea>
      <xsl:if test="//formResponse/errors/error[contains(@field, 'text')]">
        <p>
          <xsl:value-of select="//formResponse/errors/error[contains(@field, 'text')]" />
        </p>
      </xsl:if>
    </div>
    <button type="submit" class="btn btn-default">Submit</button>
  </form>
</xsl:template>

</xsl:stylesheet>

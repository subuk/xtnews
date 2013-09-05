<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template name="object-form">
  <form role="form" method="post" action="">
    <div class="form-group">
      <label for="subject">Subject</label>
      <input type="text" class="form-control" id="subject" name="subject" placeholder="Text">
        <xsl:attribute name="value">
          <xsl:value-of select="//formResponse/errors/error[contains(@field, 'subject')]" />
        </xsl:attribute>
      </input>
    </div>

    <div class="form-group">
      <label for="text">Text</label>
      <textarea id="text" name="text">
        <xsl:value-of select="//formResponse/errors/error[contains(@field, 'text')]" />
      </textarea>
    </div>
    <button type="submit" class="btn btn-default">Submit</button>
  </form>

</xsl:template>

</xsl:stylesheet>


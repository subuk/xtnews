<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="html"
  encoding="UTF-8"
  indent="yes"
  cdata-section-elements="script noscript"
  undeclare-namespaces="yes"
  omit-xml-declaration="yes"
  doctype-system="about:legacy-compat" />

<!--
<xsl:template match="doc" mode="header">
  <head>
    <link rel="stylesheet" type="text/css" charset="utf-8" href="{$shost}markup/_pages/style.css" />
  </head>
</xsl:template>
 -->

<xsl:template name="formatDate">
  <xsl:param name="datetime" />
  <xsl:value-of select="substring-before($datetime,' ')" />
</xsl:template>

<xsl:template match="objects">
  <table class="table">
    <thead>
      <tr>
        <th>#</th>
        <th>Date created</th>
        <th>Title</th>
        <th>Text</th>
        <th></th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <xsl:apply-templates />
    </tbody>
  </table>
  <a href="new/">Add</a>
</xsl:template>

<xsl:template match="object">
  <tr>
    <td><xsl:value-of select="id"/></td>
    <td>
      <xsl:call-template name="formatDate">
        <xsl:with-param name="datetime" select="date_created"/>
      </xsl:call-template>
    </td>
    <td><xsl:value-of select="title"/></td>
    <td><xsl:value-of select="text"/></td>
    <td>
      <a>
        <xsl:attribute name="href">
          <xsl:value-of select="id" /><xsl:text>/edit/</xsl:text>
        </xsl:attribute>
        <xsl:text>Edit</xsl:text>
      </a>
    </td>
    <td>
      <a>
        <xsl:attribute name="href">
          <xsl:value-of select="id" /><xsl:text>/delete/</xsl:text>
        </xsl:attribute>
        <xsl:text>Delete</xsl:text>
      </a>
    </td>
  </tr>
</xsl:template>

<xsl:template match="form">
  <xsl:variable name="titleError">
    <xsl:value-of select="errors/error[@field='title']" />
  </xsl:variable>

  <xsl:variable name="textError">
    <xsl:value-of select="errors/error[@field='text']" />
  </xsl:variable>

  <form role="form" method="post" action="">
    <div class="form-group">
      <label for="title">Title</label>
      <input type="text" class="form-control" id="title" name="title">
        <xsl:attribute name="value">
          <xsl:value-of select="values/value[@field='title']" />
          <xsl:value-of select="//object/title" />
        </xsl:attribute>
      </input>
      <xsl:if test="$titleError != ''">
        <p>
          <xsl:value-of select="$titleError" />
        </p>
      </xsl:if>
    </div>

    <div class="form-group">
      <label for="text">Text</label>
      <textarea id="text" name="text" cols="50" rows="40">
        <xsl:value-of select="values/value[@field='text']" />
        <xsl:value-of select="//object/text" />
      </textarea>

      <xsl:if test="$textError != ''">
        <p>
          <xsl:value-of select="$textError" />
        </p>
      </xsl:if>
    </div>
    <button type="submit" class="btn btn-default">Submit</button>
  </form>
</xsl:template>

<xsl:template match="deleteConfirmation">
  <form method="post" action="">
    Are you sure?
    <button class="btn" type="submit">Yes</button>
    <a href="../" class="btn">no</a>
  </form>
</xsl:template>

</xsl:stylesheet>


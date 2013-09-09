<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="html" encoding="utf-8" indent="yes" />

<xsl:template match="/">

<xsl:text disable-output-escaping='yes'>&lt;!DOCTYPE html></xsl:text>
<html>
  <head>
    <link rel="stylesheet" type="text/css" charset="utf-8" href="{{ STATIC_URL }}bootstrap/css/bootstrap.css" />
  </head>
  <body>

    <div class="container">
      <div class="header">
        <ul class="nav nav-pills pull-right">
          <li><a href="/new/">add</a></li>
        </ul>
        <h3 class="text-muted"><a href="/">xtNews</a></h3>
      </div>

      <div class="row marketing">
        <xsl:apply-templates />
      </div>
    </div> <!-- /container -->
  </body>
</html>
</xsl:template>

<xsl:template name="formatDate">
  <xsl:param name="datetime" />
  <xsl:value-of select="substring-before($datetime,' ')" />
</xsl:template>

<xsl:template match="objects">
  
  <table class="table">
    <thead>
      <tr>
        <th>#</th>
        <th>Title</th>
        <th>Date created</th>
        <th></th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <xsl:apply-templates />
    </tbody>
  </table>
</xsl:template>

<xsl:template match="//doc/objects/object">
  <tr>
    <td><xsl:value-of select="id"/></td>
    <td>
      <a>
        <xsl:attribute name="href">
          <xsl:value-of select="id" /><xsl:text>/</xsl:text>
        </xsl:attribute>
        <xsl:value-of select="title"/>
      </a>
    </td>
    <td>
      <xsl:call-template name="formatDate">
        <xsl:with-param name="datetime" select="date_created"/>
      </xsl:call-template>
    </td>
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

<xsl:template match="//doc/object">
  <h2>
    <xsl:value-of select="title" />
  </h2>
  <div class="content">
    <xsl:value-of select="text" />
  </div>
  <hr />
  <p>
  <xsl:call-template name="formatDate">
    <xsl:with-param name="datetime" select="date_created"/>
  </xsl:call-template>
  </p>
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
      <textarea class="form-control" rows="20" id="text" name="text">
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
    Are you sure you want to delete this article?
    <button class="btn btn-success" type="submit">Yes</button>
    <a href="../" class="btn">No</a>
  </form>
</xsl:template>

</xsl:stylesheet>


#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create html page
"""

import re
import json
import fileinput

# http://davidbau.com/archives/2011/09/09/python_templating_with_stringfunction.html
from templet import unicodefunction

@unicodefunction
def myTemplate(db):
    """
<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>台灣立法院議事錄 Taiwan Congress Journals</title>
<!-- Bootstrap -->
<link href="css/bootstrap.min.css" rel="stylesheet">
<style>
  body {
    padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
  }
</style>
</head>
<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="brand" href="#">Open Data</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="#">Home</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
<div class="container">
<div class="hero-unit">
<h2>立法院議事錄</h2>
<p>尋找立法院的開會記錄嗎？此網站收集立法院第六屆起的議事錄，歡迎使用及推廣。</p><p>立法院管理系統提供的原始的資料格式為Word doc以及html，為了方便分析，我們亦提供純文字格式。</p>
</div>
<ul>
${{
    for key in sorted(db, key=db.get, reverse=True):
        item = db[key]
        s = '<li id="%s">%s (%s) <a id="%s" href="%s">doc</a> <a id="%s" href="%s">html</a> <a id="%s" href="%s">txt</a> %s</li>\\n' % (key, item['session'], item['category'], key+"-doc", item['doc_mirror'], key+"-html", item['html_mirror'], key+"-txt", item['txt'], changeDateFormat(item['date']) )
        out.append(s.encode('utf-8'))
}}
</ul>
<div><a href="journals_link.json">檔案連結:JSON格式</a></div>
<div><a href="http://lci.ly.gov.tw/">資料來源:立法院議事暨公報管理系統</a></div>
</div>
</body>
</html>
"""

def changeDateFormat(date):
    date = re.sub(r'(\d+)/(\d+)/(\d+)', ur'\1年\2月\3日', date)
    date = u'議期:民國%s' % date
    return date

if __name__ == '__main__':
    db = json.loads(''.join(fileinput.input()))
    print myTemplate(db)

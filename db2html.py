#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create html page
"""

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
<h1>立法院議事錄</h1>
<ul>
${{
    for key in sorted(db, key=db.get):
        item = db[key]
        s = '<li id="%s">%s %s <a id="%s" href="%s">doc</a> <a id="%s" href="%s">html</a></li>\\n' % (key, item['category'], item['session'], key+"-doc", item['doc'], key+"-html", item['html'])
        out.append(s.encode('utf-8'))
}}
</ul>
<div><a href="journals_link.json" class="btn btn-primary">JSON格式</a></div>
<div><a href="http://lci.ly.gov.tw/">資料來源:立法院議事暨公報管理系統</a></div>
</div>
</body>
</html>
"""

if __name__ == '__main__':
    db = json.loads(''.join(fileinput.input()))
    print myTemplate(db)

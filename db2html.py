#!/usr/bin/env python
# -*- coding: utf-8 -*-
from templet import stringfunction,unicodefunction
import json

@unicodefunction
def myTemplate(db):
    """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Taiwan Congress Journals</title>
</head>
<body>
<ul>
${{
    for key in sorted(db, key=db.get):
        item = db[key]
        out.append('<li id="%s">%s %s <a id="%s" href="%s">doc</a> <a id="%s" href="%s">html</a></li>\\n' %
        (key, item['category'], item['session'], key+"-doc", item['doc'], key+"-html", item['html']) )
}}
</ul>
<div><a href="http://lci.ly.gov.tw/">Data Source</a></div>
<div><a href="https://raw.github.com/jyunfan/ly_crawler/master/data/journals_link.json">JSON format</div>
</body>
</html>
    """

db = json.loads(open('journals_link.json').read())
print myTemplate(db).encode('utf-8')

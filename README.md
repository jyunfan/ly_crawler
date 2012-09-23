ly_crawler
==========

Extract links of journals from Taiwanese Congress website.
Data come from http://lci.ly.gov.tw/lcew/index_5.zul

Requirement
-----------
* Firefox 15+
* Firebug 1.10+  https://addons.mozilla.org/zh-TW/firefox/addon/firebug/
* Greasemonkey 1.0  https://addons.mozilla.org/zh-TW/firefox/addon/greasemonkey/
* Python 2.7+

Installation
------------
# Make sure you installed Greasemonkey, a Firefox add-on
# Download source from https://github.com/jyunfan/ly_crawler/zipball/master
# Extract the zip file.
# Open lci_link_extractor.user.js in Firefox.  Follow the instruction.

Usage
-----
# $ python lci_link.py
# Open Firefox and go to url http://lci.ly.gov.tw/lcew/index_5.zul  You will see the page changes automatically.  Please wait about 15 minutes.
# Open the source directory and find the output link.db
# $ python shelve2json.py link > link.json

Example Data
------------
Feel free to take a glance of links.
We have 2 formats now: data/journals_link.html and data/journals_link.json

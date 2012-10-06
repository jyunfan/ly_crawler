#!/usr/bin/env python
""" Add local links to ly db """

import shelve
from sys import argv

if len(argv)<2:
    print """Usage add_local_link.py db"""
    exit(0)

db = shelve.open(argv[1], writeback=True)
if db == None:
    print "Cannot open db %s" % argv[1]
    exit(1)

for key in db:
    db[key]['doc_mirror']  = 'data/%s.doc'  % key
    db[key]['html_mirror'] = 'data/%s.html' % key
    db[key]['txt']         = 'data/%s.txt'  % key
db.close()

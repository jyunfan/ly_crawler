#!/usr/bin/env python
import shelve
import json
from sys import argv

if len(argv)<=1:
    print 'Usage: shelve2json.py [shelvedb]'
    exit(0)

db = dict(shelve.open(argv[1]))
print json.dumps(db)

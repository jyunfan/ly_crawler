#!/usr/bin/env python
import shelve
from sys import argv

if len(argv)<=1:
    exit(0)

db = shelve.open(argv[1])
for key in db:
    print "key:" + key
    print db[key]
db.close()

#!/usr/bin/env python
""" Receive and store entry into databases
"""

from bottle import post, route, run, request
import shelve

def convert2dict(bottledict):
    d = {}
    for key in bottledict:
        d[key] = bottledict[key]
    return d

@route('/hello')
def hello():
    return "Hello World!"

@post('/<dbname>/<key>')
def link_add(dbname, key):
    db = shelve.open(dbname)
    db[key] = convert2dict(request.POST)
    db.close()

run(host='', port=8080, debug=True)

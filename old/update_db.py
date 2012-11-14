#!/usr/bin/env python
"""
Start a web service to receive and store key-value into Python shelve
database.
"""

from bottle import post, run, request
import os
import shelve

def convert2dict(bottledict):
    ''' Convert a bottle object to pure dict object '''
    d = {}
    for key in bottledict:
        d[key] = bottledict[key]
    return d

@post('/<dbname>/<key>')
def add_entry(dbname, key):
    '''
    Store values in POST request to db.
    Return 0 if the key does not exist, return 1 otherwise.
    '''
    db = shelve.open(os.path.join('data', dbname))

    if db.has_key(key):
        is_exists = '1'
    else:
        is_exists = '0'

    db[key] = convert2dict(request.POST)
    db.close()
    return is_exists

run(host='', port=8080, debug=True)

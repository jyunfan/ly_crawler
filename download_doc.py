#!/usr/bin/env python
""" Download doc and html fies from lci.ly.gov.tw """

import sys
import json
import urllib
import fileinput
import os.path
from time import sleep

def get_url(url, filename):
    """ Download file if the file is not existed """
    pos = url.rfind('/')
    if pos == -1:
        return

    if os.path.isfile(filename):
        return

    urllib.urlretrieve(url, filename)
    sleep(1)

if __name__ == '__main__':
    try:
        db = json.loads(''.join(fileinput.input()))
    except:
        print "Usage: get_doc.py db.json"
        exit(1)

    for key in db:
        get_url(db[key]['doc'], os.path.join('data', key + '.doc'))
        get_url(db[key]['html'], os.path.join('data', key + '.html'))

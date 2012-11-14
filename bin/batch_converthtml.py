#!/usr/bin/env python
""" Convert all html files under data/data to plain text """

import os
import glob

htmlfiles = glob.glob('data/*.html')
for htmlfile in htmlfiles:
    textfile = os.path.splitext(htmlfile)[0] + '.txt'
    if not os.path.isfile(textfile):
        os.system('html2plaintxt.py %s' % htmlfile)


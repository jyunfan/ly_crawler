#!/usr/bin/env python
""" Extract content from html and save to plain text """

import os
import re
import sys
import fileinput
# 3rd party lib
import lxml.html

def condenseEmptyLines(text):
    return re.sub(r'\n{2,}', '\n\n', text)

def removeLonglyWhiteSpace(text):
    return re.sub(r'^\s+$', '', text, 0, re.MULTILINE)

def removeComments(text):
    return re.sub(r'<!--[\d\D]*?-->', '', text)

def convert(htmlfile):
    textfile = os.path.splitext(htmlfile)[0] + '.txt'
    print "Convert html %s to plain text %s" % (htmlfile, textfile)

    html = lxml.html.parse(htmlfile)

    text = html.getroot().text_content()

    # clean text
    text = removeComments(text)
    text = removeLonglyWhiteSpace(text)
    text = condenseEmptyLines(text)

    f = open(textfile, 'w')
    f.write(text.encode('utf-8'))
    f.close()

if __name__ == '__main__':
    if len(sys.argv)<2:
        print "Usage html2plaintext.py a.html"
        exit(1)
    convert(sys.argv[1])


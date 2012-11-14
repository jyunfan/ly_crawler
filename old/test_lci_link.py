#!/usr/bin/env python
import urllib
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
f = urllib.urlopen("http://localhost:8080/link/yatta", params)
print f.read()


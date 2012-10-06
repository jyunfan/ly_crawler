#!/usr/bin/env python
import json

journals = json.loads(open('journals_link.json', 'r').read())
for j in journals:
    print journals[j]['session'] + ':' + journals[j]['doc']

#!/bin/bash
./shelve2json.py data/journals_link.db | ./db2html.py > data/journals_link.html

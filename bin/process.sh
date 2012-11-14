#!/bin/bash

DATADIR=../data
# Collect links
scrapy crawl lci

# add local links
./add_local_link.py $DATADIR/journals_link.db

# convert db to json format
./shelve2json.py $DATADIR/journals_link.db > $DATADIR/journals_link.json

# create html
./db2html.py $DATADIR/journals_link.json > $DATADIR/journals_link.html

OPATH=$PATH
PATH=$PATH:`pwd`
# Download files
pushd .
cd $DATADIR; download_doc.py journals_link.json
popd

# Convert journals from html format to plain format
pushd .
cd $DATADIR; batch_converthtml.py
popd

PATH=$OPATH

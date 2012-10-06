#!/bin/bash
# Run this script after collecting links

./add_local_link.py data/journals_link.db
./shelve2json.py data/journals_link.db > data/journals_link.json
./db2html.py data/journals_link.json > data/journals_link.html

# Download files
pushd .
cd data; ../download_doc.py journals_link.json
popd

./batch_converthtml.py

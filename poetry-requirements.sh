#!/bin/sh

command -v poetry >/dev/null 2>&1 || { echo >&2 "I require poetry but it's not installed. Aborting."; exit 0; }

poetry export --without-hashes -n --without-urls| cut -f1 -d";" | sed 's/ *$//g' > requirements/base.txt

echo /dev/null > requirements/production.txt
echo "-r base.txt\n" > requirements/production.txt
poetry export --without-hashes --only prod -n --without-urls| cut -f1 -d";" | sed 's/ *$//g' >> requirements/production.txt


echo /dev/null > requirements/local.txt
echo "-r production.txt\n" > requirements/local.txt
poetry export --without-hashes --only dev -n --without-urls| cut -f1 -d";" | sed 's/ *$//g' >> requirements/local.txt

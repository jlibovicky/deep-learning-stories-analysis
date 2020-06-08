#!/bin/bash

DIR=websites/github.com/blog

cd websites/github.com
for F in $(find blog -maxdepth 1 -mindepth 1 -type d); do
    if [ -e $F/index.html ]; then
        SUBDIR=$(grep 'content="20..-[01][0-9]-[0-3][0-9] ..:..:.. UTC"' $F/index.html | sed -e 's/.*content="\(20..-[01][0-9]\)-[0-3][0-9] ..:..:.. UTC".*/\1/;s#-#/#')
        mkdir -p $DIR/$SUBDIR
        mv $F $DIR/$SUBDIR/
    fi
done

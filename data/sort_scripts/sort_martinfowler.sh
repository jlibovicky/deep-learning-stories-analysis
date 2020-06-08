#!/bin/bash

DIR=websites/martinfowler.com

for F in $(find $DIR/articles -maxdepth 1 -mindepth 1 -type f -name '*.html'); do
    DATE=$(grep "<p class = 'date'>" "$F" | sed -e 's/<\/p>.*$//;s/.*>//')
    if [[ ! -z "$DATE" ]]; then
        YEAR=$(echo $DATE | sed 's/.* //')
        MONTH=$(echo $DATE | sed 's/ 20..$//;s/.* //;s/January/01/;s/February/02/;s/March/03/;s/April/04/;s/May/05/;s/June/06/;s/July/07/;s/August/08/;s/September/09/;s/October/10/;s/November/11/;s/December/12/')
        mkdir -p $DIR/$YEAR/$MONTH
        mv $F $DIR/$YEAR/$MONTH
    fi
done

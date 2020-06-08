#!/bin/bash

DIR=websites/davidwalsh.name

for F in $(find $DIR -maxdepth 1 -mindepth 1 -type d); do
    echo $F
    if [ -e "$F/index.html" ]; then
        DATE=$(grep '<time>' "$F/index.html" | sed -e 's/<\/time>.*$//;s/.*>//')
        YEAR=$(echo $DATE | sed -e 's/.*, //')
        MONTH=$(echo $DATE | sed -e 's/ .*//;s/January/01/;s/February/02/;s/March/03/;s/April/04/;s/May/05/;s/June/06/;s/July/07/;s/August/08/;s/September/09/;s/October/10/;s/November/11/;s/December/12/')
        SUBDIR="$YEAR/$MONTH"

        if [[ $SUBDIR =~ 20[0-1][0-9]/[0-1][0-9] ]]; then
            mkdir -p $DIR/$SUBDIR
            mv $F $DIR/$SUBDIR
        fi
    fi
done

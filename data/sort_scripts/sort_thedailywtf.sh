#!/bin/bash

cd websites/thedailywtf.com/articles

for F in *; do
    DATE=$(grep datePublished "$F/index.html" | sed -e 's#</span>##;s/.*>//;' | strings)
    if [[ $DATE =~ ^20[0-1][0-9]-[0-1][0-9]-[0-3][0-9]$ ]]; then
        YEAR=$(echo $DATE | sed -e 's/-.*//')
        MONTH=$(echo $DATE | sed -e 's/-..$//;s/^....-//')
        SUBDIR="../$YEAR/$MONTH/"
        mkdir -p $SUBDIR
        mv "$F" $SUBDIR
        echo $F to $SUBDIR
    else
        rm -r "$F"
        echo removed $F
    fi
done

#!/bin/bash

cd websites/www.hanselman.com/blog

for F in *.aspx; do
    DATE=$(grep blogMetaDate $F | sed -e 's/<\/span>.*//;s/.*>//')
    MONTH_WORD=$(echo $DATE | sed 's/ .*//')
    YEAR=$(echo $DATE | sed "s/.*'/20/")
    MONTH=$(echo $MONTH_WORD | sed -e 's/January/01/;s/February/02/;s/March/03/;s/April/04/;s/May/05/;s/June/06/;s/July/07/;s/August/08/;s/September/09/;s/October/10/;s/November/11/;s/December/12/')
    SUBDIR=$YEAR/$MONTH

    if [[ $SUBDIR =~ ^20[0-1][0-9]/[0-1][0-9]$ ]]; then
        mkdir -p $SUBDIR
        TGT_FILE=$(echo $F | sed -e 's/aspx$/html/')
        mv $F $SUBDIR/$TGT_FILE
    else
        rm $F
    fi
done

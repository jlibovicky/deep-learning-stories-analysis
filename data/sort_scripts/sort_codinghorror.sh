#!/bin/bash

DIR=websites/blog.codinghorror.com/

for F in $(find $DIR -maxdepth 1 -mindepth 1 -type d); do
    echo $F
    if [ -e $F/index.html ]; then
        SUBDIR=$(grep '<time datetime="' $F/index.html | sed -e 's/.*datetime="//;s/".*//;s#-#/#;s/...$//')
        echo $SUBDIR
        mkdir -p $DIR/$SUBDIR
        mv $F $DIR/$SUBDIR/
    fi
done

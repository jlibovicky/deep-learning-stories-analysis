#!/bin/bash

for CATEGORY in developers researchers technology_fans; do
    for WEBSITE in $(cat categories/$CATEGORY.txt); do
        find tf_idf/$WEBSITE -type f | \
        while read FILE; do
            KEYWORD_COUNT=$(head -n 100 $FILE | grep 'deep learning\|machine learning\|artificial intelligence' | wc -l)
            if [ $KEYWORD_COUNT -ge 1 ]; then
                echo $FILE
            fi
        done
    done > relevant_"$CATEGORY".txt
done

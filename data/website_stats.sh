#!/bin/bash

for WEBSITE_DIR in websites/*; do
    NAME=$(echo $WEBSITE_DIR | sed -e 's#websites/##')
    HTML_COUNT=$(for YEAR in {2012..2016}; do find $WEBSITE_DIR/$YEAR -type f; done | wc -l)
    HTML_COUNT_FORMATED=$(LC_NUMERIC=en_US printf "%'d" $HTML_COUNT)
    TEXT_COUNT=$(for YEAR in {2012..2016}; do find plain_text/$NAME/$YEAR -type f; done | wc -l)
    TEXT_COUNT_FORMATED=$(LC_NUMERIC=en_US printf "%'d" $TEXT_COUNT)
    PROPORTION=$(echo 100 \* $TEXT_COUNT / $HTML_COUNT | bc -l)
    WORD_COUNT=$(for YEAR in {2012..2016}; do find plain_text/$NAME/$YEAR -type f -exec cat {} \; ; done | wc -w)
    WORD_COUNT_FORMATED=$(LC_NUMERIC=en_US printf "%'d" $WORD_COUNT)


    echo "$NAME    &    $TEXT_COUNT_FORMATED    &    $WORD_COUNT_FORMATED    &    $HTML_COUNT_FORMATED    &    ${PROPORTION%.*}\\% \\\\"
done

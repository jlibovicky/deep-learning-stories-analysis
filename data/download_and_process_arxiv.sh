#!/bin/bash

for YEAR in {2017..2017}; do
    for MONTH in {01..12}; do
        for START in 01 11 21; do
            END=$(($START + 10))
            echo "$YEAR/$MONTH"
            wget "http://export.arxiv.org/oai2?verb=ListRecords&set=cs&from=$YEAR-$MONTH-$START&until=$YEAR-$MONTH-$END&metadataPrefix=arXiv" -O arxiv.xml
            python process_arxiv_xml.py arxiv.xml
            sleep 1m
        done
    done
done

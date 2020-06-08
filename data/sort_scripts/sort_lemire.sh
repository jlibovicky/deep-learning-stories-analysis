#!/bin/bash

DIR=websites/lemire.me/blog

for YEAR in {2004..2017}; do
    for MONTH in {01..12}; do
        for DAY in {01..31}; do
            mv $DIR/$YEAR/$MONTH/$DAY/* $DIR/$YEAR/$MONTH/
        done
    done
done


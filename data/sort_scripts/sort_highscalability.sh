#!/bin/bash

DIR=websites/highscalability.com

for YEAR in {2012..2017}; do
    for MONTH in {1..12}; do
        for DAY in {1..31}; do
            mv $DIR/$YEAR/$MONTH/$DAY/* $DIR/$YEAR/$MONTH
        done
    done
done

for YEAR in {2012..2017}; do
    for MONTH in {1..9}; do
        mv $DIR/$YEAR/$MONTH $DIR/$YEAR/0$MONTH
    done
done

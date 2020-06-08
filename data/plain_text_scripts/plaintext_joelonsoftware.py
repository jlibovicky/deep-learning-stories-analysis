#!/usr/bin/env python

import sys
import re


def main():
    fist_headline = False
    has_started = False

    for line in sys.stdin:
        line = line.rstrip()

        if line.startswith('# '):
            has_started = fist_headline
            fist_headline = True

        if line.startswith('## Want to know more'):
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

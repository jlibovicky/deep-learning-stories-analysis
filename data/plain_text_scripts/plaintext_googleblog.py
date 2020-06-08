#!/usr/bin/env python

import sys
import re


def main():
    seen_first_headline = False
    has_started = False

    for line in sys.stdin:
        line = line.rstrip()

        if not seen_first_headline and line.startswith('#'):
            seen_first_headline = True
            continue

        if seen_first_headline and line.startswith('#'):
            has_started = True

        if line == 'Google' or line == '> Google':
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

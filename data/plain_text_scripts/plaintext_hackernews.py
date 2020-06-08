#!/usr/bin/env python

import sys
import re


def main():
    has_started = False

    for line in sys.stdin:
        line = line.rstrip()

        if line.startswith('#'):
            has_started = True

        if re.match('^201[2-6]-[01][0-9]-[0-3][0-9]T', line):
            continue

        if line == '##### Comments':
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

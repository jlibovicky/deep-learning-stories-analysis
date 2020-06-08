#!/usr/bin/env python

import sys
import re

def main():
    has_started = False

    for line in sys.stdin:
        line = line.rstrip()

        if re.match(r'^##  [A-Za-z]', line):
            has_started = True

        if re.match(r'^[0-9]+ Kudos', line):
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

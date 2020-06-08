#!/usr/bin/env python

import sys
import re


def main():
    has_started = False

    for line in sys.stdin:
        line = line.rstrip()

        if line.startswith('# '):
            has_started = True

        if re.match(r'^201[2-6]-[01][0-9]-$', line):
            continue

        if line.startswith('### Share this:'):
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

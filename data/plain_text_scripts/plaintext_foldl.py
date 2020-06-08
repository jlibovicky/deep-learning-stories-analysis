#!/usr/bin/env python

import sys
import re


def main():
    has_started = False
    first_headline = False

    for line in sys.stdin:
        line = line.rstrip()

        if line.startswith('# '):
            has_started = first_headline
            first_headline = True

        if re.match(r'^[0-9].*201[2-6]$', line):
            continue

        if line.startswith('## Related Posts'):
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

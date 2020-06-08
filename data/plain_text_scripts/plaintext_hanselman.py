#!/usr/bin/env python

import sys
import re


def main():
    has_started = False

    for line in sys.stdin:
        line = line.rstrip()

        if line.startswith('Sponsored By'):
            has_started = True
            continue

        if (line.startswith('| [Blog Home]')
                or line.startswith('«')
                or 'Related Links' in line):
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

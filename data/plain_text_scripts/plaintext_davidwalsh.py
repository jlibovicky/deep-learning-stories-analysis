#!/usr/bin/env python

import sys
import re


def main():
    has_started = False
    skip_lines = 0

    for line in sys.stdin:
        line = line.rstrip()

        if skip_lines > 0:
            skip_lines -= 1
            continue

        if re.match(r'^# [A-Za-z]', line):
            has_started = True
            skip_lines = 5

        if line == '## Discussion':
            exit()

        if has_started:
            if line.startswith('>'):
                print(line[1:])
            else:
                print(line)


if __name__ == "__main__":
    main()

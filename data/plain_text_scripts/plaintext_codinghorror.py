#!/usr/bin/env python

import sys
import re


def main():
    has_started = False

    for line in sys.stdin:
        line = line.rstrip()

        if line.startswith('# Coding Horror'):
            continue

        if re.match(r'^# [A-Za-z]', line):
            has_started = True

        if (line.startswith('[advertisement]') or
                line == 'Next'):
            exit()

        if has_started:
            if line.startswith('>'):
                print(line[1:])
            else:
                print(line)


if __name__ == "__main__":
    main()

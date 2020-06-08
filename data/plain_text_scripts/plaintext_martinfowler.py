#!/usr/bin/env python

import sys
import re


def main():
    has_started = False
    skip_lines = 0
    removing_contents = False

    for line in sys.stdin:
        line = line.rstrip()

        if skip_lines > 0:
            skip_lines -= 1
            continue

        if re.match(r'^# [A-Za-z]', line):
            has_started = True

        if line == '## Contents':
            removing_contents = True
            continue

        if removing_contents:
            if line and line[0] != ' ':
                removing_contents = False
            else:
                continue

        if line == 'Martin Fowler':
            continue

        if re.match('[0-9].*20[0-1][0-9]', line):
            continue

        if line.startswith('Find similar'):
            continue

        if line == '* * *':
            continue

        if line == 'Share:':
            exit()

        if has_started:
            if line.startswith('>'):
                print(line[1:])
            else:
                print(line)


if __name__ == "__main__":
    main()

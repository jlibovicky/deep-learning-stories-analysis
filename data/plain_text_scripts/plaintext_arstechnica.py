#!/usr/bin/env python

import sys
import re

def main():
    has_started = False

    for line in sys.stdin:
        line = line.rstrip()

        if line == '# ArsTechnica':
            continue

        if re.match(r'^# [A-Za-z]', line):
            has_started = True

        if (line == 'reader comments' or line.startswith('Page: ') or line == 'Reader comments'
                or line == 'Expand full story'):
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

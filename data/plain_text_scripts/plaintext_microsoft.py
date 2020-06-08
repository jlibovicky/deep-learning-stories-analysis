#!/usr/bin/env python

import sys
import re


def main():
    has_started = False
    lines_to_skip = 0

    for line in sys.stdin:
        line = line.rstrip()

        if re.match(r'^# +[A-Za-z]', line):
            has_started = True
            lines_to_skip = 20

        if lines_to_skip > 0:
            lines_to_skip -= 1
            continue

        if (line.startswith('Back to')
                or line.startswith('#### Related Posts:')):
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

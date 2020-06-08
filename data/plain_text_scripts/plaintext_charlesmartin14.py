#!/usr/bin/env python

import sys
import re

def main():
    has_started = False

    for line in sys.stdin:
        line = line.rstrip()

        if line == '# Machine Learning':
            continue

        if re.match(r'^# [A-Za-z]', line):
            has_started = True

        if (re.match(r'.*Share this.*', line) or
            re.match(r'[0-9]+ Comments$', line) or
            line == '1 Comment' or
            line == 'about these ads' or
            line == 'About these ads' or
            line == 'Leave a comment'):
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

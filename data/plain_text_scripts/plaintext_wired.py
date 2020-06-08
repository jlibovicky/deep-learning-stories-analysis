#!/usr/bin/env python

import sys


def main():
    has_started = False
    first_headline = False

    for line in sys.stdin:
        line = line.rstrip()

        if line.startswith('# '):
            has_started = first_headline
            first_headline = True

        if line.startswith('  *   *'):
            continue

        if (line.startswith('Go Back to Top') or
                line.startswith('Skip Social.')):
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

#!/usr/bin/env python

import sys


def main():
    has_started = False

    for line in sys.stdin:
        line = line.rstrip()

        if line.startswith('Next Story'):
            has_started = True
            continue

        if has_started and line.startswith('  * ##### '):
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

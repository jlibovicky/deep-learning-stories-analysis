#!/usr/bin/env python

import sys
import re


def main():
    has_started = False

    for line in sys.stdin:
        line = line.rstrip()

        if line.startswith('### '):
            has_started = True

        if line.startswith('Posted by hal'):
            exit()

        if has_started:
            print(line)


if __name__ == "__main__":
    main()

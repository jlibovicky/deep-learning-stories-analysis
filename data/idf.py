#!/usr/bin/env python

import sys
import codecs

def main():
    vocabulary = {}
    document_frequencies = {}
    term_count = 0
    document_count = 0
    for i, file_name in enumerate(sys.stdin):
        document_count += 1
        in_document = set()
        try:
            with open(file_name.rstrip(), encoding='utf-8') as f_term:
                for line in f_term:
                    term_count += 1
                    term = line.rstrip()
                    in_document.add(term)
                    if term not in vocabulary:
                        vocabulary[term] = 1
                    else:
                        vocabulary[term] += 1

            for term in in_document:
                if term not in document_frequencies:
                    document_frequencies[term] = 1
                else:
                    document_frequencies[term] += 1
        except UnicodeEncodeError:
            print("Unicode error: {}".format(file_name), file=sys.stderr)
            pass
        print("Processed {} documents.\r".format(i + 1),
              file=sys.stderr, end='')
    print('\n', file=sys.stderr)

    for term in sorted(vocabulary, key=lambda t: -vocabulary[t]):
        print("{}\t{}\t{}\t{}\t{}".format(
            term,
            vocabulary[term],
            vocabulary[term] / term_count,
            document_frequencies[term],
            document_frequencies[term] / document_count))


if __name__ == "__main__":
    main()

#!/usr/bin/env python

import sys
import math
from argparse import ArgumentParser


def main(document_count, idf_table_file):
    idf_table = {}

    with open(idf_table_file, encoding="utf-8") as f_idf:
        for line in f_idf:
            word, _, _, doc_count, _ = line.rstrip().split('\t')
            idf_table[word] = math.log(document_count / int(doc_count))

    term_frequencies = {}
    term_count = 0
    for line in sys.stdin:
        term = line.rstrip()
        if term not in idf_table:
            continue
        term_count += 1
        if term not in term_frequencies:
            term_frequencies[term] = 1
        else:
            term_frequencies[term] += 1

    tfidf_scored = [
        (term, term_frequencies[term] / term_count * idf_table[term])
        for term in term_frequencies]

    for term, score in sorted(tfidf_scored, key=lambda x: -x[1]):
        print("{}\t{}".format(term, score))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("document_count", type=int)
    parser.add_argument("idf_table_file")
    args = parser.parse_args()
    main(args.document_count, args.idf_table_file)

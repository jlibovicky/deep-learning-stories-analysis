#!/usr/bin/env python

from argparse import ArgumentParser
import os


def main(keyword, root, directories):
    for year in [2012, 2013, 2014, 2015, 2016]:
        for quartal in range(4):
            score = score_from_quartal(
                year, quartal, keyword, root, directories)
            print(score)


def score_from_quartal(year, quartal, keyword, root, directories):
    score_sum = 0.
    doc_count = 0
    for quartal_month in range(3):
        year_month = 3 * quartal + quartal_month + 1
        for directory in directories:
            explore_dir = os.path.join(
                    root, directory, str(year), "{:02d}".format(year_month))
            for dir_root, _, files in os.walk(explore_dir):
                for file_name in files:
                    file_path = os.path.join(dir_root, file_name)
                    score_sum += score_from_file(keyword, file_path)
                    doc_count += 1
    if doc_count == 0:
        return 0.
    return 1000 * score_sum / doc_count


def score_from_file(keyword, file_path):
    with open(file_path, encoding="utf-8") as f_tfidf:
        for line, _ in zip(f_tfidf, range(100)):
            term, _ = line.rstrip().split('\t')
            if term == keyword:
                return 1.
    return 0.


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("keyword", type=str)
    parser.add_argument("root_directory", type=str)
    parser.add_argument("directories", nargs='*', type=str)
    args = parser.parse_args()

    main(args.keyword, args.root_directory, args.directories)

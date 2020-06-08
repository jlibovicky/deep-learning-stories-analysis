#!/usr/bin/env python

from argparse import ArgumentParser
import os
import math

import numpy as np


def main(vocabulary_file, keyword, root, directories):
    vocabulary = read_vocabulary(vocabulary_file)

    for year in [2012, 2013, 2014, 2015, 2016]:
        print("YEAR {}".format(year))
        print("===================")

        scores_table = scores_from_year(year, vocabulary, root, directories)
        keyword_correlations = correlations(keyword, vocabulary, scores_table)

        for i in range(min(20, len(keyword_correlations))):
            term, corr = keyword_correlations[i]
            print("+ {} ({:.3f})".format(term, corr))

        print()


def read_vocabulary(vocabulary_file):
    vocabulary = []
    with open(vocabulary_file, encoding='utf-8') as f_vocab:
        for line in f_vocab:
            vocabulary.append(line.rstrip())
    return vocabulary


def scores_from_year(year, vocabulary, root, directories):
    scores = []
    for month in range(1, 13):
        for directory in directories:
            explore_dir = os.path.join(
                root, directory, str(year), "{:02d}".format(month))
            for dir_root, _, files in os.walk(explore_dir):
                for file_name in files:
                    file_path = os.path.join(dir_root, file_name)
                    file_scores = file_to_vocab_list(vocabulary, file_path)
                    scores.append(file_scores)
    return np.array(scores)


def correlations(keyword, vocabulary, scores_table):
    corel_matrix = np.corrcoef(scores_table, rowvar=False)

    # get keyword index
    keyword_index = vocabulary.index(keyword)

    # argsort
    sort_indices = np.argsort(-corel_matrix[keyword_index])

    # return sorted tuples (term, correlation)
    sorted_terms = [(vocabulary[i], corel_matrix[i, keyword_index])
                    for i in sort_indices
                    if not math.isnan(corel_matrix[keyword_index, i])]
    return sorted_terms


def file_to_vocab_list(vocabulary, file_path):
    file_dict = {}
    with open(file_path, encoding="utf-8") as f_tfidf:
        for rank, line in enumerate(f_tfidf):
            term, score_str = line.rstrip().split('\t')
            file_dict[term] = 1  # float(score_str)
            if rank >= 100:
                break

    scores_list = [file_dict.get(term, 0.) for term in vocabulary]
    norm = np.linalg.norm(scores_list)
    return [s / norm for s in scores_list]


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("keyword", type=str)
    parser.add_argument("vocabulary", type=str)
    parser.add_argument("root_directory", type=str)
    parser.add_argument("directories", nargs='*', type=str)
    args = parser.parse_args()

    main(args.vocabulary, args.keyword, args.root_directory,
         args.directories)

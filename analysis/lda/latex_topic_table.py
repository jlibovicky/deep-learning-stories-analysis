#!/usr/bin/env python

from argparse import ArgumentParser


def main(labels_file, words_file):
    print('\\begin{tabular}{lp{.8\\textwidth}}')
    print('\\toprule')
    print('topic label & topic words and weights \\\\ \\hline')

    with open(labels_file, 'r', encoding='utf-8') as f_labels, \
            open(words_file, 'r', encoding='utf-8') as f_words:
        for label, words in zip(f_labels, f_words):
            sum_terms = [w.split('*') for w in words.rsplit(' + ')]
            word_score_pairs = [
                format_pair(w[1].strip('"'), w[0]) for w in sum_terms]
            print("{} & {} \\\\".format(label.rstrip(),
                                        ", ".join(word_score_pairs)))

    print('\\bottomrule')
    print('\\end{tabular}')


def format_pair(word, score):
    return "{}~{{\small ({})\}}".format(word.replace(' ', '~'), score[1:])


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("labels_file", type=str)
    parser.add_argument("words_file", type=str)
    args = parser.parse_args()

    main(args.labels_file, args.words_file)

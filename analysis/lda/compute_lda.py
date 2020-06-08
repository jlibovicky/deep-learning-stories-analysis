#!/usr/bin/env python

from argparse import ArgumentParser
import os

from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel
import numpy as np


def main(root_dir, file_list, num_topics, output_dir):
    doc_list, quartal_table = load_documents(root_dir, file_list)
    print("Documents loaded in memory.")

    lda, dictionary = compute_lda(doc_list, num_topics)
    print("LDA analysis finished, formating output.")
    os.mkdir(output_dir)
    print_topics(lda, output_dir)
    print("Gathering timelines.")
    print_timeline(lda, dictionary, quartal_table, output_dir)
    print("Done.")


def load_documents(root_dir, file_list):
    doc_list = []
    quartal_table = {y: {i: [] for i in range(0, 4)}
                     for y in [2012, 2013, 2014, 2015, 2016]}
    with open(file_list, 'r', encoding='utf-8') as f_list:
        for i, line in enumerate(f_list):
            file_path = os.path.join(root_dir, line.rstrip())
            _, _, year_str, month_str, *_ = line.split('/')
            year = int(year_str)
            quartal = int(month_str) // 4
            try:
                with open(file_path, encoding='utf-8') as f_doc:
                    doc = [line.rstrip() for line in f_doc]
                doc_list.append(doc)
                quartal_table[year][quartal].append(doc)
            except UnicodeEncodeError:
                pass
            print("\rLoaded {} documents".format(i + 1), end='')
    print()
    return doc_list, quartal_table


def compute_lda(doc_list, num_topics):
    dictionary = Dictionary(doc_list)
    dictionary.filter_extremes(no_below=2, no_above=0.5)
    _ = dictionary[0]
    print("Converting docs to BOW vectors.")
    corpus = [dictionary.doc2bow(doc) for doc in doc_list]

    print("Computing LDA.")
    lda = LdaModel(corpus, num_topics=num_topics, id2word=dictionary)
    return lda, dictionary


def print_topics(lda, output_dir):
    path = os.path.join(output_dir, "topic_words.txt")
    with open(path, 'w', encoding='utf-8') as f_topics:
        for topic in lda.print_topics(num_words=15):
            print(topic[1], file=f_topics)


def print_timeline(lda, dictionary, quartal_table, output_dir):
    path = os.path.join(output_dir, "topic_timeline.txt")
    with open(path, 'w', encoding='utf-8') as f_timeline:
        for year in [2012, 2013, 2014, 2015, 2016]:
            for quartal in range(4):
                qurtal_sum = np.zeros(shape=[lda.num_topics])
                quartal_count = 0
                for doc in quartal_table[year][quartal]:
                    bow = dictionary.doc2bow(doc)
                    topics = lda.get_document_topics(bow)
                    for topic_id, score in topics:
                        qurtal_sum[topic_id] += score
                    quartal_count += 1
                quartal_avg = (qurtal_sum / quartal_count if quartal_count > 0
                               else qurtal_sum)
                print(",".join(str(x) for x in quartal_avg), file=f_timeline)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("root_dir", type=str)
    parser.add_argument("file_list", type=str)
    parser.add_argument("num_topics", type=int)
    parser.add_argument("output_dir", type=str)
    args = parser.parse_args()

    main(args.root_dir, args.file_list, args.num_topics, args.output_dir)

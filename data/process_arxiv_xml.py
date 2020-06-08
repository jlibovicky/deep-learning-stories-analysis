#!/usr/bin/env python

import argparse
import os
import xml.etree.ElementTree as ET


RELEVANT_CATS = set(['cs.AI', 'cs.CL', 'cs.CV', 'cs.NE'])


def main(xml_file):

    root = ET.parse(xml_file).getroot()
    record_list = root.find(
        '{http://www.openarchives.org/OAI/2.0/}ListRecords')

    for paper in record_list:
        metadata = paper.find(
            '{http://www.openarchives.org/OAI/2.0/}metadata')

        if not metadata:
            continue

        paper_data = metadata.find('{http://arxiv.org/OAI/arXiv/}arXiv')
        paper_id = paper_data.find('{http://arxiv.org/OAI/arXiv/}id').text
        year_str = paper_id[:2]
        month_str = paper_id[2:4]
        categories = paper_data.find(
            '{http://arxiv.org/OAI/arXiv/}categories').text.split()

        if not year_str.isdigit() or int(year_str) < 12 or int(year_str) > 16:
            continue
        if not RELEVANT_CATS.intersection(categories):
            continue

        paper_dir = os.path.join("plain_text", "arxiv",
                                 "20" + year_str, month_str)
        os.makedirs(paper_dir, exist_ok=True)

        abstract = paper_data.find(
            '{http://arxiv.org/OAI/arXiv/}abstract').text
        title = paper_data.find('{http://arxiv.org/OAI/arXiv/}title').text

        abstract_file = os.path.join(paper_dir, paper_id)
        with open(abstract_file, 'w') as f_abs:
            print(title, file=f_abs)
            print('', file=f_abs)
            print(abstract, file=f_abs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xml_file", type=str)
    args = parser.parse_args()

    main(args.xml_file)

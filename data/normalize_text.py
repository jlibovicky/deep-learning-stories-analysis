#!/usr/bin/env python

import re
import sys

import spacy
from spacy.matcher import Matcher
from spacy.attrs import IS_PUNCT, LOWER


def main():
    nlp = spacy.load('en')

    matcher = Matcher(nlp.vocab)
    matcher.add_pattern(
        "deep_learning", [{LOWER: "deep"}, {LOWER: "learning"}])
    matcher.add_pattern(
        "artificial_intelligence",
        [{LOWER: "artificial"}, {LOWER: "intelligence"}])
    matcher.add_pattern(
        "machine_learning", [{LOWER: "machine"}, {LOWER: "learning"}])
    matcher.add_pattern(
        "reinforcement_learning",
        [{LOWER: "reinforcement"}, {LOWER: "learning"}])
    matcher.add_pattern(
        "pattern_recognition", [{LOWER: "parttern"}, {LOWER: "recognition"}])
    matcher.add_pattern(
        "computer_vision", [{LOWER: "computer"}, {LOWER: "vision"}])
    matcher.add_pattern(
        "machine_vision", [{LOWER: "machine"}, {LOWER: "vision"}])
    matcher.add_pattern(
        "machine_translation", [{LOWER: "machine"}, {LOWER: "vision"}])

    text = re.sub(r'\s+', ' ', sys.stdin.read())

    doc = nlp(text)
    entities = list(doc.ents)
    matches = matcher(doc)

    skip_until = -1
    for i, token in enumerate(doc):
        if i < skip_until:
            continue

        if matches:
            _, _, start, end = matches[0]
            if i == start:
                print(doc[start:end].lemma_.lower())
                skip_until = end
                matches.pop(0)

        if token.is_alpha and not token.is_stop and token.ent_iob_ == 'O':
            print(token.lemma_.lower())

        if (token.ent_iob_ == 'B' and
                token.ent_type_ not in ['DATE', 'TIME', 'MONEY', 'PERCENT',
                                        'QUANTITY', 'ORDINAL', 'CARDINAL']):
            entity = entities.pop(0)
            print(entity.lemma_.lower())


if __name__ == "__main__":
    main()

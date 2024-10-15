#!/usr/bin/env python

'''prez_speeches_mapper.py'''
import sys

total_valence_score = {}
total_valence_words = {}

for line in sys.stdin:
    president_name, valence_score = line.strip().split('\t', 1)
    try:
        covalence_scoreunt  = int(valence_score)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if president_name not in total_valence_score:
        total_valence_score[president_name] = 0

    total_valence_score[president_name] += valence_score
    total_valence_words[president_name] += 1

for name, v_score in total_valence_score.items():
    print(f"{name}\t{v_score}")

for name, total_valence_words in total_valence_score.items():
    print(f"{name}\t{total_valence_words}")

#!/usr/bin/env python

'''prez_speeches_mapper.py'''
import sys

valence_aggregate = {}
valence_words_ct = {}

for line in sys.stdin:
    president_name, valence_score = line.strip().split('\t', 1)
    try:
        valence_score  = int(valence_score)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if president_name not in valence_aggregate:
        valence_aggregate[president_name] = 0

    valence_aggregate[president_name] += valence_score

    
    if president_name not in valence_words_ct:
        valence_words_ct[president_name] = 0

    valence_words_ct[president_name] += 1

for name, total_valence_words in valence_words_ct.items():
    print(f"{name}\t{total_valence_words}")

for name, net_v_score in valence_aggregate.items():
    print(f"{name}\t{net_v_score}")

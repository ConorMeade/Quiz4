#!/usr/bin/env python3

'''prez_speeches_reducer.py'''
import sys

total_valence_score = 0
num_words = 0
president_name = 'missing name'
for line in sys.stdin:
    line = line.strip()
    president_name, valence_score = line.split('\t', 1)
    try:
        valence_score  = int(valence_score)
        total_valence_score += valence_score
        num_words += 1
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

print(f"{president_name}\ttotal\t{num_words}")
print(f"{president_name}\t\t{total_valence_score}")

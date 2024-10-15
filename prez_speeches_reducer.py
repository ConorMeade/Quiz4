#!/usr/bin/env python3

'''prez_speeches_reducer.py'''
import sys

# valence_aggregate = {}
# valence_words_ct = {}
total_valence_score = 0
num_words = 0
president_name = 'missing name'
for line in sys.stdin:
# with open('adams.txt', 'r') as c:
    president_name, valence_score = line.strip().split('\t', 1)
    try:
        valence_score  = int(valence_score)
        total_valence_score += valence_score
        num_words += 1
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    # if president_name not in valence_aggregate:
    #     valence_aggregate[president_name] = 0


    # valence_aggregate[president_name] += valence_score
    
    # if president_name not in valence_words_ct:
    #     valence_words_ct[president_name] = 0

    # valence_words_ct[president_name] += 1

print(f"{president_name}\ttotal\t{num_words}")
print(f"{president_name}\t\t{total_valence_score}")
# for name, total_valence_words in valence_words_ct.items():
#     print(f"{name}\ttotal\t{total_valence_words}")

# for name, net_v_score in valence_aggregate.items():
#     print(f"{name}\t{net_v_score}")

#!/usr/bin/env python3

'''prez_speeches_reducer.py'''
import sys

total_valence_score = 0
num_words = 0
president_name = 'missing name'

presidents_valence_score = {}
presidents_total_valence_words = {}
for line in sys.stdin:
    president_name, valence_score = line.strip().split('\t', 1)
    try:
        valence_score  = int(valence_score)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if president_name not in presidents_valence_score:
        presidents_valence_score[president_name] = valence_score
    else:
        presidents_valence_score[president_name] += valence_score
    
    if president_name not in presidents_total_valence_words:
        presidents_total_valence_words[president_name] = 0
    else:
        presidents_total_valence_words[president_name] += 1

for name, total_valence_words in presidents_total_valence_words.items():
    print(f"{name}\t{total_valence_words}")

for name, net_v_score in presidents_valence_score.items():
    print(f"{name}\ttotal\t{net_v_score}")
    
    # line = line.strip()
    # president_name, valence_score = line.split('\t', 1)
    # try:
    #     valence_score  = int(valence_score)
    # except ValueError:
    #     # count was not a number, so silently
    #     # ignore/discard this line
    #     continue
    # if president_name not in presidents_valence_score:
    #     presidents_valence_score[president_name] = valence_score
        
    # else:
    #     presidents_valence_score[president_name] += valence_score

    # if president_name not in presidents_total_valence_words:
    #     presidents_total_valence_words[president_name] = 1
    # else:
    #     presidents_total_valence_words[president_name] += 1


# for president_name, num_words in  presidents_total_valence_words.items():
#     print(f"{president_name}\ttotal\t{num_words}")

# for president_name, valence_score in presidents_valence_score:
#     print(f"{president_name}\t\t{valence_score}")

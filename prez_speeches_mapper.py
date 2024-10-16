#!/usr/bin/env python3


'''prez_speeches_mapper.py'''
import sys
import re
import requests
import string
import os

stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
stopwords = list(set(stopwords_list.decode().splitlines()))
valence_words_data = requests.get("https://raw.githubusercontent.com/fnielsen/afinn/master/afinn/data/AFINN-en-165.txt").content
valencewords = list(set(valence_words_data.decode().splitlines()))
valence_dict = {}

for v in valencewords:
    word, score = v.split('\t')
    valence_dict[word] = score

def remove_stopwords(words):
    list_ = re.sub(r"[^a-zA-Z0-9]", " ", words.lower()).split()
    return [itm for itm in list_ if itm not in stopwords]

def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('[\d\n]', ' ', text)
    return ' '.join(remove_stopwords(text))

def valence(text):
    return calc_valence(text)

def calc_valence(text):
    v = []
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    text_list = text.split(' ')
    for w in text_list:
        if w in valence_dict:
            v.append(valence_dict[w])
            # print(f"{president_name}\t{valence_dict[w]}")

    return v

# def main(argv):
def main(argv):
    president_name = 'missing prez name'
    line = sys.stdin.readline()
    try:
        while line:
            clean_line = clean_text(line) # returns a line as a space-seperated line, or a sentence if you will
            # fetch president name
            if "mapreduce_map_input_file" in os.environ:
                president_file_name = os.environ['mapreduce_map_input_file']
                president_name = re.sub(r'.*/|_speeches_\d+\.txt$', '', president_file_name)
            valence_vals = valence(clean_line)
            for v in valence_vals:
                print(f"{president_name}\t{v}")
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)
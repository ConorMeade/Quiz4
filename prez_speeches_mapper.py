#!/usr/bin/env python


'''prez_speeches_mapper.py'''
import sys
import re
import requests
import string

stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
stopwords = list(set(stopwords_list.decode().splitlines()))
valence_list = requests.get("https://raw.githubusercontent.com/fnielsen/afinn/master/afinn/data/AFINN-en-165.txt").content
valencewords = list(set(valence_list.decode().splitlines()))
valence_tuples = []
for v in valencewords:
    word, score = v.split('\t')
    valence_tuples.append((word, int(score)))


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
    # valence_score = 0
    filter_sentence = remove_stopwords(text)
    filter_sentence = clean_text(filter_sentence)
    words = filter_sentence.split(' ')
    for w in words:
        for v in valence_tuples:
            if w.strip() == v[0]:
                print(f'{v[0]}\t{v[1]}')
                # valence_score += v[1]
    # print(f'{text[:10]}...\t{valence_score}')
    # return f'{text[:10]}...\t{valence_score}'

def main(argv):
    line = sys.stdin.readline()
    sentences = line.split('.')
    # pattern = re.compile(r'\"(\w+)\s')
    try:
        while line:
            sentences = line.split('.')
            for s in sentences:
                print(valence(s))
        line = sys.stdin.readline()
                
    except EOFError as error:
        return None


if __name__ == "__main__":
    main(sys.argv)
#!/usr/bin/env python


'''prez_speeches_mapper.py'''
import sys
import re
import requests
import string
import io
import tarfile

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

def valence(text, president_name):
    return calc_valence(text, president_name)

def calc_valence(text, president_name):
    filter_sentence = remove_stopwords(text)
    filter_sentence = clean_text(filter_sentence)
    words = filter_sentence.split(' ')
    for w in words:
        if w in valence_dict:
            print(f'{president_name}\t{valence_dict[word]}')

def process_tar_file(f):
    with tarfile.open(fileobj=f, mode="r:gz") as tar:
        for member in tar.getmembers():
            if member.isfile():
                file_name = member.name
                president_name = re.sub(r'_speeches_*', '', file_name)
                speech_file = tar.extractfile(member)
                if speech_file is not None:
                    for line in speech_file:
                        valence(line, president_name)
                        # clean_line = clean_text(line.decode('utf-8'))

                        # clean_line_list = clean_line.split(' ')
                        # for word in clean_line_list:
                        #     if word in valence_dict:
                                # print(f'{president_name}\t{valence_dict[word]}')s


def main(argv):
    for input in sys.stdin:
        process_tar_file(input.strip())


if __name__ == "__main__":
    main(sys.argv)
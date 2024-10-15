#!/usr/bin/env python


'''prez_speeches_mapper.py'''
import sys
import re
import requests
import string
import os
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
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    no_stop_words = remove_stopwords(text)
    filter_sentence = []
    for f in no_stop_words:
        filter_sentence.append(clean_text(f))
    for w in filter_sentence:
        if w in valence_dict:
            print(f"{president_name}\t{valence_dict[w]}")
            # print(f"{president_name}\t a")

def process_tar_file(f):
    # with tarfile.open(fileobj=f, mode="r:gz") as tar:
    if '.tar' in f:
        with tarfile.open(f, mode="r:gz") as tar:
            for member in tar.getmembers():
                if member.isfile():
                    file_name = member.name
                    name_pattern = r'^(.*?)/'
                    president_name = re.match(name_pattern, file_name).group(1)
                    speech_file = tar.extractfile(member)
                    if speech_file is not None:
                        for line in speech_file:
                            valence(line.decode('utf-8').strip(), president_name)
    else:
        pass
    # return valence_vals

# def main(argv):
def main(argv):
    # for input in sys.stdin:
    #     # print(input)
    #     process_tar_file(input.strip())
    president_name = 'foo'
    # file_name = os.getenv("mapreduce_map_input_file")
    # # file_name = "fdroosevelt_speeches_000.txt"
    name_pattern = r'^(.*?)_'
    # # print(file_name)
    # match = re.match(name_pattern, file_name)
    # if match:
    #     president_name = match.group(1)
        # print(president_name)
    line = sys.stdin.readline()

    # fetch president name
    # <president name>/speeches as txt files
    try:
        while line:
            # fetch president name
            president_file_name = os.environ['mapreduce_map_input_file']
            match = re.match(name_pattern, president_file_name)
            if match:
                president_name = match.group(1)
            valence(line, president_name)
        line = sys.stdin.readline()
    except EOFError as error:
        return None
            
    # valence_vals = 0
    # process_tar_file("adams.tar.gz")
    # for president, valence in valence_vals.items():
        # print(f"{president}\t{valence}")


if __name__ == "__main__":
    main(sys.argv)
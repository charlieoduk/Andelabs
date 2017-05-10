import collections
from collections import Counter

def words(string):
    if type(string) == str:
        split_string = phrase.split()
        word_occurence = dict(Counter(split_string))
        for key in word_occurence.keys():
            try:
                int(key)
                word_occurence[int(key)] = word_occurence.pop(key)
            except ValueError:
                continue
        return word_occurence
    else:
        raise TypeError
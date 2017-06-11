# -*- coding: utf-8 -*-
"""
Created on Sun May 28 12:26:16 2017 """

import nltk
from nltk import ngrams
from collections import Counter

tweets = []

corpus = open('lemmatized_ironic.txt', 'r', encoding='utf-8')

for line in corpus:
    tweets.append(line)

corpus.close

allbigrams = []

for line in tweets:
    token = nltk.word_tokenize(line)
    bigrams = [" ".join(pair) for pair in ngrams(token,2)]
    for item in bigrams:
        allbigrams.append(item)

c = Counter(allbigrams).most_common(None)

f = open('countbigraminsirony.txt', 'w', encoding='utf-8')

for item in c:
    f.write(str(item))
    f.write('\n')

f.close

alltrigrams = []

for line in tweets:
    token = nltk.word_tokenize(line)
    trigrams = [" ".join(pair) for pair in ngrams(token,3)]
    for item in trigrams:
        alltrigrams.append(item)

c = Counter(alltrigrams).most_common(None)

f = open('counttrigramsirony.txt', 'w', encoding='utf-8')

for item in c:
    f.write(str(item))
    f.write('\n')

f.close
  
#text = "It begins on an ordinary day. Except he misses out on what happens during the morning and afternoon hours of his daily life. His ‘day’ usually starts in the evening and carries on into the late night and early hours of the morning where he spends most of his time recording and editing videos."
#token = nltk.word_tokenize(text)
#bigrams = [" ".join(pair) for pair in ngrams(token,2)]
#c = Counter(bigrams)
#print (Counter(bigrams).most_common(None))
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:01:07 2017

"""
import csv
import re

icorpus = open('ironyf.txt', 'r', encoding='utf-8').readlines()
ncorpus = open('non_irony.txt', 'r', encoding='utf-8').readlines()

excl = []
quest = []
quotes = []
indot = []
dash = []
tweetlength = []
emots = []
label = []
tweets = []

for i in icorpus:
    i = i.strip()
    ex = len(re.findall('!', i))
    excl.append(ex)
    que = len(re.findall('\?', i))
    quest.append(que)
    quotes.append(len(re.findall('["«].*?["»]', i)))
    indot.append(len(re.findall('\.{2,}', i)))
    dash.append(len(re.findall(' \- ', i)))
    tweetlength.append(len(i))
    emots.append(len(re.findall(':\(', i)))
    label.append('irony')
    tweets.append(i)
    
for i in ncorpus:
    i = i.strip()
    ex = len(re.findall('!', i))
    excl.append(ex)
    que = len(re.findall('\?', i))
    quest.append(que)
    quotes.append(len(re.findall('["«].*?["»]', i)))
    indot.append(len(re.findall('\.{2,}', i)))
    dash.append(len(re.findall(' \- ', i)))
    tweetlength.append(len(i))
    emots.append(len(re.findall(':\(', i)))
    label.append('nonirony')
    tweets.append(i)    
    
features = open('features.csv', 'w', encoding = 'utf-8')
features.write('id\ttext\texcl\tquest\tquotes\tindot\tdash\tlength\temots\tlabel\n')

for i in range(len(label)):
    tweet = tweets[i]
    line = [str(i), str(tweet.strip()), str(excl[i]), str(quest[i]), str(quotes[i]), str(indot[i]), 
            str(dash[i]), str(tweetlength[i]), str(emots[i]), str(label[i])]
    features.write('\t'.join(line)+'\n')
    
features.close()


    
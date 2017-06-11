# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 01:35:50 2017


"""
import re
from pymystem3 import Mystem


ironic = open('ironyf.txt', 'r', encoding='utf-8')
nonironic = open('non_irony.txt', 'r', encoding='utf-8')
lemi = open('lemmatized_ironic.txt', 'w', encoding='utf-8')
lemn = open('lemmatized_non.txt', 'w', encoding='utf-8')

m = Mystem()

listir = []
listnon = []

for i in ironic:
        i = re.sub(r'[^\w\s]', ' ', i)
        i = m.lemmatize(i)
        listir.append(i)

for i in nonironic:
        i = re.sub(r'[^\w\s]', ' ', i)
        i = m.lemmatize(i)
        listnon.append(i)
        
for i in listir:
    lemi.write(str(i) + '\n')

for i in listnon:
    lemn.write(str(i) + '\n')
        
lemi.close()
lemn.close()
        
ironic.close()
nonironic.close()

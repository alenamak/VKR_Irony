# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:05:45 2017

"""

from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
from imblearn.pipeline import make_pipeline
from imblearn.metrics import classification_report_imbalanced
from collections import Counter
import pandas

df = pandas.read_csv('features.csv', sep = '\t', index_col='id')
feats = ['excl', 'excl', 'quest', 'quotes', 'indot', 'dash', 'length', 'emots']
X, y = df[feats], df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
c = Counter(list(y_train))
print (c)
pipeline = make_pipeline(RandomOverSampler(),
                         RandomForestClassifier(n_estimators=500))
pipeline.fit(X_train, y_train)

print(classification_report_imbalanced(y_test, pipeline.predict(X_test)))
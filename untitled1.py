# -*- coding: utf-8 -*-
"""
Created on Mon May 29 22:15:52 2017

@author: Portgas D. Ace
"""

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import TruncatedSVD
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler
from imblearn.pipeline import make_pipeline
from imblearn.metrics import classification_report_imbalanced

df = pandas.read_csv('features.csv', sep = '\t', index_col='id')
X, y = df['text'], df['label']
tfidf_vectorizer = CountVectorizer(max_df=0.5, min_df=5)
tfidf = tfidf_vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(tfidf, y, test_size=0.2)
#svd = TruncatedSVD(n_components=100)
#X = svd.fit_transform()
#print(tfidf_vectorizer.vocabulary_)
 
#numpy.savetxt("unigrams.csv", tfidf, delimiter='\t')

pipeline = make_pipeline(TruncatedSVD(n_components=100),
                         RandomOverSampler(),
                         RandomForestClassifier(n_estimators=100))
pipeline.fit(X_train, y_train)

print(classification_report_imbalanced(y_test, pipeline.predict(X_test)))

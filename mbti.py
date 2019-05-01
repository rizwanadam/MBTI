# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:35:54 2019

@author: Rizwan1
"""

import pandas as pd
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()

data = pd.read_csv("D:\\typed_comments.csv",chunksize=1)
df = pd.DataFrame(columns=['comment'])
j=0

for i in data:
    #split  into words
    tokens = word_tokenize(i.iat[0,19])
    #convert to lower case
    tokens = [w.lower() for w in tokens]
    #remove punctuation
    table = str.maketrans('','',string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    #retain alphabetic elements
    words = [word for word in stripped if word.isalpha()]
    #remove stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    #stem
    stemmed = [porter.stem(word) for word in words]
    
    df.append({'comment':stemmed},ignore_index=True,sort=None,verify_integrity=False)
    j=j+1
    if j==1000:
        break;
    
df.to_csv('out4.csv',mode='w')
    
    
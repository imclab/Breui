# -*- coding: utf-8 -*-

from gensim import corpora
from gensim import models
from gensim import similarities
import codecs

def vec_tuple2feature(tupleVect):
    featureVect = []
    for i in range(len(tupleVect)):
        tuple = tupleVect[i]
        featureVect.append(tuple[1])
    return(featureVect)

def doc_tuple2feature(tupleCorpus):
    featureDoc = []
    for x in tupleCorpus:
        tmp = []
        for i in range(len(x)):
            y = x[i]
            tmp.append(y[1])
        featureDoc.append(tmp)
    return featureDoc
    
    
    
# Carica un corpus di documenti
corpus = corpora.MmCorpus('.//Corpus/corpus.mm')
print corpus

dict = corpora.Dictionary.load('.//Corpus/corpus.dict')
#print dictionary
#print dictionary.token2id

tfidfmodel = models.TfidfModel(corpus)
corpus_tfidf = tfidfmodel[corpus]
#tfidf.save('.//Corpus/corpus_tfidf.tfidf')

lsimodel = models.LsiModel(corpus_tfidf, num_topics=30)
corpus_lsi = lsimodel[tfidfmodel[corpus]]
#lsi.save('.//Corpus/corpus_lsi.lsi')

import numpy as np

doc = doc_tuple2feature(corpus_lsi)
print doc


matrix = np.array(doc)
print matrix
print matrix.shape

ave_doc = np.average(doc,0)
std_doc = np.std(doc,0)

import numpy as np
import pylab as pl
import matplotlib.font_manager
from sklearn import svm
  
# fit the model
clf = svm.OneClassSVM(nu=0.2, kernel="rbf", gamma=0.1)
clf.fit(matrix)

# predizione sul train dataset
y_pred_train = clf.predict(matrix)
print y_pred_train

#Legge la query per fare un test
f = codecs.open(".//Corpus//prova_notizia.txt", encoding='utf-8')
doc = f.read()
f.close()
#doc = u"pippo pluto e paperino napoli gol"

#attenzione il DOC a doc2bow deve essere una lista di word
vec_bow = dict.doc2bow(doc.lower().split())
#convert query to tfidf model
vec_tfidf = tfidfmodel[vec_bow]
# convert the query to LSI space
vec_lsi = lsimodel[vec_tfidf]
print vec_lsi

vec_test = vec_tuple2feature(vec_lsi)
print vec_test

y_pred_test = clf.predict(vec_test)
print y_pred_test



# -*- coding: utf-8 -*-
'''
Created on 26/apr/2013
(Big luck!!)
Esegue query tramite uno stimatore Gaussiano One Class

@author: Francesco Collova
'''

import numpy as np
from sklearn import svm
from gensim import corpora
from gensim import models
import codecs
import pickle
from util import *

import pylab as pl


RootDir = ".//DataFile"

# Carica un corpus di documenti
corpus = corpora.MmCorpus(RootDir + '//Corpus/corpus.mm')
print corpus

#Legge il dizionario
dictionary = corpora.Dictionary.load(RootDir + '//Corpus/corpus.dict')

#print dictionary
#print dictionary.token2id

#carica il modell TFIDF
tfidfmodel = models.TfidfModel.load(RootDir + '//Corpus//corpus_tfidf.tfidf')

#Carica il modello LSI
lsimodel = models.LsiModel.load(RootDir + '//Corpus//corpus_lsi.lsi')

corpus_lsi = lsimodel[tfidfmodel[corpus]]

doc = doc_tuple2feature(corpus_lsi)
print "Features: ", doc

matrix = np.array(doc)
print matrix
print matrix.shape

ave_doc = np.average(doc,0)
std_doc = np.std(doc,0)

  
# fit the model
clf = svm.OneClassSVM(nu=0.2, kernel="rbf", gamma=0.1)
clf.fit(matrix)
pickle.dump(clf, open( RootDir + "//Corpus//OneClass.pic", "wb" ) )
clf = pickle.load( open( RootDir + "//Corpus//OneClass.pic", "rb" ) )

# predizione sul train dataset
y_pred_train = clf.predict(matrix)
print y_pred_train

#Legge la query per fare un test
f = codecs.open(".//Corpus//prova_calcio.txt", encoding='utf-8')
doc = f.read()
f.close()
#doc = u"pippo pluto e paperino napoli giocano a calcio e la partita è finita Juventus"

#attenzione il DOC a doc2bow deve essere una lista di word
vec_bow = dictionary.doc2bow(doc.lower().split())
#convert query to tfidf model
vec_tfidf = tfidfmodel[vec_bow]
# convert the query to LSI space
vec_lsi = lsimodel[vec_tfidf]
print vec_lsi

vec_test = vec_tuple2feature(vec_lsi)
print vec_test

AA= np.array(vec_test)
print "Train test", AA

y_pred_test = clf.predict(AA)
print y_pred_test

y_decision = clf.decision_function(AA)
print y_decision


# Plotting
X_train=matrix

xx, yy = np.meshgrid(np.linspace(-2, 2, 500), np.linspace(-2, 2, 500))# plot the line, the points, and the nearest vectors to the plane
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
pl.title("Novelty Detection")
pl.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=pl.cm.Blues_r)
a = pl.contour(xx, yy, Z, levels=[0], linewidths=2, colors='red')
pl.contourf(xx, yy, Z, levels=[0, Z.max()], colors='orange')

b1 = pl.scatter(X_train[:, 0], X_train[:, 1], c='white')
pl.show()

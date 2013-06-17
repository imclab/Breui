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

# Solo per il plotting

# import pylab as pl


RootDir = "..//DataFile"

# Carica un corpus di documenti
corpus = corpora.MmCorpus(RootDir + '//Corpus/corpus.mm')
print corpus

#Legge il dizionario
dictionary = corpora.Dictionary.load(RootDir + '//Corpus/corpus.dict')

#print dictionary
#print dictionary.token2id

#Carica il modello LSI
lsimodel = models.LsiModel.load(RootDir + '//Corpus//corpus_lsi_no_tfidf.lsi')

corpus_lsi = lsimodel[corpus]

doc = doc_tuple2feature(corpus_lsi)
print "Features: ", doc

matrix = np.array(doc)
print matrix
print matrix.shape

ave_doc = np.average(doc,0)
std_doc = np.std(doc,0)

  
# fit the model
clf = svm.OneClassSVM(nu=0.4, kernel="rbf", gamma=0.1)
clf.fit(matrix)
pickle.dump(clf, open( RootDir + "//Corpus//OneClass_no_tfidf.pic", "wb" ) )
clf = pickle.load( open( RootDir + "//Corpus//OneClass_no_tfidf.pic", "rb" ) )

# predizione sul train dataset
y_pred_train = clf.predict(matrix)
print y_pred_train



# Plotting
# 
# X_train=matrix
# xx, yy = np.meshgrid(np.linspace(-15, 15, 500), np.linspace(-15, 15, 500))# plot the line, the points, and the nearest vectors to the plane
# Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)
# pl.title("Novelty Detection")
# pl.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=pl.cm.Blues_r)
# a = pl.contour(xx, yy, Z, levels=[0], linewidths=2, colors='red')
# pl.contourf(xx, yy, Z, levels=[0, Z.max()], colors='orange')
# b1 = pl.scatter(X_train[:, 0], X_train[:, 1], c='white')
# pl.show()

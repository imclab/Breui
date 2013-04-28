# -*- coding: utf-8 -*-
'''
Created on 27/apr/2013
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

RootDir = ".//TestFile"
RootCorpora = ".//DataFile"

# Carica un corpus di documenti
corpus = corpora.MmCorpus(RootCorpora + '//Corpus/corpus.mm')
print corpus
#Legge il dizionario
dictionary = corpora.Dictionary.load(RootCorpora + '//Corpus/corpus.dict')

#carica il modell TFIDF
tfidfmodel = models.TfidfModel.load(RootCorpora + '//Corpus//corpus_tfidf.tfidf')

#Carica il modello LSI
lsimodel = models.LsiModel.load(RootCorpora + '//Corpus//corpus_lsi.lsi')


#legge lo stimatore
clf = pickle.load( open( RootCorpora + "//Corpus//OneClass.pic", "rb" ) )

y_pred_test = []
y_decision = []
for root, dirs, files in os.walk(RootDir):
    for file in filter(lambda file: file.endswith('.txt'), files):
        #Legge la query per fare un test
        document = codecs.open(os.path.join(root, file), encoding='utf-8').read() # read the entire document, as one big string
        #attenzione il DOC a doc2bow deve essere una lista di word
        vec_bow = dictionary.doc2bow(document.lower().split())
        print vec_bow
        #convert query to tfidf model
        vec_tfidf = tfidfmodel[vec_bow]
        # convert the query to LSI space
        vec_lsi = lsimodel[vec_tfidf]
        vec_test = vec_tuple2feature(vec_lsi)
        #Test se la lista dei termini è vuota
        if vec_test :
            print vec_test
            test_array= np.array(vec_test)
            print test_array
            y_pred_test.append(clf.predict(test_array))
            y_decision.append(clf.decision_function(test_array))
        else:
            y_pred_test.append('-1')
            
#        print file, y_pred_test, y_decision

print y_pred_test
print "Goodness", len([x for x in y_pred_test if x < 0])/float(len(y_pred_test))

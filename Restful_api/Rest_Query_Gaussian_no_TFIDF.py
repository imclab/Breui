# -*- coding: utf-8 -*-
'''
Created on 27/apr/2013
(Big luck!!)
Esegue query tramite uno stimatore Gaussiano One Class

@author: Francesco Collova
'''

import os
import numpy as np
from sklearn import svm
from gensim import corpora
from gensim import models
import codecs
import pickle
from Classification.util import *




def Test_SVN(document):
    RootDir = "..//TestFile"
    RootCorpora = "..//DataFile"# Carica un corpus di documenti
    corpus = corpora.MmCorpus(RootCorpora + '//Corpus/corpus.mm')
    #Legge il dizionario
    dictionary = corpora.Dictionary.load(RootCorpora + '//Corpus/corpus.dict')
    print dictionary.token2id

    #Carica il modello LSI
    lsimodel = models.LsiModel.load(RootCorpora + '//Corpus//corpus_lsi_no_tfidf.lsi')
    #legge lo stimatore
    clf = pickle.load( open( RootCorpora + "//Corpus//OneClass_no_tfidf.pic", "rb" ) )
    #attenzione il DOC a doc2bow deve essere una lista di word
    vec_bow = dictionary.doc2bow(List_of_Word(document))
    print vec_bow
    # convert the query to LSI space
    vec_lsi = lsimodel[vec_bow]
    print vec_lsi
    vec_test = vec_tuple2feature(vec_lsi)
    #Test se la lista dei termini è vuota
    if vec_test :
        test_array= np.array(vec_test)
        pred = clf.predict(test_array)
        test = clf.decision_function(test_array)
    else:
        pred = -1
        test = 255
    print "< Pred:%i, Dist:%f >" % (pred, test)     
    return pred, test

# -*- coding: utf-8 -*-

from gensim import corpora
from gensim import models
from gensim import similarities


RootDir = ".//DataFile"

# Carica un corpus di documenti
corpus = corpora.MmCorpus(RootDir + '//Corpus/corpus.mm')
print corpus

dictionary = corpora.Dictionary.load(RootDir + '//Corpus/corpus.dict')
print dictionary
print dictionary.token2id



lsi = models.LsiModel(corpus, num_topics=2)
lsi.save(RootDir + '//Corpus/corpus_lsi_no_tfidf.lsi')


#Stampa i cluster dell'LSI
for topicN in range(lsi.num_topics):
    print 'topic %i: %s \n' % (topicN, lsi.print_topic(topicN))

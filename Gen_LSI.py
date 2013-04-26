# -*- coding: utf-8 -*-

from gensim import corpora
from gensim import models
from gensim import similarities



# Carica un corpus di documenti
corpus = corpora.MmCorpus('.//Corpus/corpus.mm')
print corpus

dictionary = corpora.Dictionary.load('.//Corpus/corpus.dict')
print dictionary
print dictionary.token2id

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
tfidf.save('.//Corpus/corpus_tfidf.tfidf')

lsi = models.LsiModel(corpus_tfidf, num_topics=24)
lsi.save('.//Corpus/corpus_lsi.lsi')


#Stampa i cluster dell'LSI
for topicN in range(lsi.num_topics):
    print 'topic %i: %s \n' % (topicN, lsi.print_topic(topicN))

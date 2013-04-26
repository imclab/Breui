# -*- coding: utf-8 -*-

'''
Created on 16/apr/2013
(Big luck!!)
Crea i dizionari a partire da un insiame di TXT

@author: Francesco Collova
'''




from gensim import *
from Iter_corpus import *


# create a corpus dictionary
corpus = MyCorpus('.//DataFile') 

for vector in corpus: # convert each document to a bag-of-word vector
    print vector

print list(corpus)
print corpus.dictionary.id2token

# Save Corpus
corpora.MmCorpus.serialize('.//Corpus//corpus.mm', corpus)
corpus.dictionary.save('.//Corpus/corpus.dict')

corpus = corpora.MmCorpus('.//Corpus/corpus.mm')
print corpus
dictionary = corpora.Dictionary.load('.//Corpus//corpus.dict')
print dictionary.token2id

# #Stampa i cluster dell'LSI
# for topicN in range(corpus.num_terms):
#     print 'topic %i: %s \n' % (topicN, corpus..print_topic(topicN))
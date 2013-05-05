# -*- coding: utf-8 -*-
'''
Created on 16/apr/2013
(Big luck!!)
Esegue query di somiglianza con un dizionario

@author: Francesco Collova
'''

from gensim import corpora
from gensim import models
from gensim import similarities
import codecs
import numpy


RootDir = ".//DataFile"

corpus = corpora.MmCorpus(RootDir + '//Corpus/corpus.mm')
print corpus

dict = corpora.Dictionary.load(RootDir + '//Corpus//corpus.dict')
print dict

#carica il modell TFIDF
tfidfmodel = models.TfidfModel.load(RootDir + '//Corpus//corpus_tfidf.tfidf')

#Carica il modello LSI
lsimodel = models.LsiModel.load(RootDir + '//Corpus//corpus_lsi.lsi')


f = codecs.open('.//Corpus//prova_notizia.txt', encoding='utf-8')
doc = f.read()
f.close()
#doc = u"pippo pluto e paperino napoli"

#attenzione il DOC a doc2bow deve essere una lista di word
vec_bow = dict.doc2bow(doc.lower().split())

#convert query to tfidf model
vec_tfidf = tfidfmodel[vec_bow]
print vec_tfidf

# convert the query to LSI space
vec_lsi = lsimodel[vec_tfidf]
print vec_lsi

index = similarities.docsim.MatrixSimilarity(lsimodel[tfidfmodel[corpus]])
#index = similarities.docsim.MatrixSimilarity(lsi[corpus])

# perform a similarity query against the corpus
sims = index[vec_lsi]

#print (document_number, document_similarity) 2-tuples
lista = list(sims)
print sorted(lista)

#print numpy.mean([A[1] for A in sims])
print numpy.mean(sims)
print float(len([x for x in sims if x > 0.5]))/len(sims)



#tfidf = models.TfidfModel(corpus)
#corpus_tfidf = tfidf[corpus]
#
#index = similarities.Similarity('C://', tfidf[corpus],num_features=3)
#print index

#lsi = models.LsiModel(corpus, id2word=dictionary.id2token, num_topics = 2)
#index = similarities.MatrixSimilarity(lsi[corpus])

#doc = "Sport"
#vec_bow = dictionary.doc2bow(doc.lower().split())
#print vec_bow
#
#vec_tfidf =tfidf[vec_bow]
#print vec_tfidf
#
#sims = index[vec_tfidf]
#
#print list(enumerate(sims))


#print corpus.dictionary.token2id
#tfidf_trans = models.tfidfmodel.TfidfModel(corpus, id2word=corpora.dictionary)
#tfidf_corpus = corpora.Mncorpus(corpus=tfidf_trans[corpus], id2word=corpora.dictionary)
#lsi_trans = models.LsiModel(corpus=tfidf_corpus, id2word=corpora.dictionary, num_features=400)

#from gensim.similarities import Similarity
#index = Similarity(corpus=lsi_transformation[logent_transformation[corpus]], num_features=400, output_prefix="shard")
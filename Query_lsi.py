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



corpus = corpora.MmCorpus('.//Corpus/corpus.mm')
print corpus

dictionary = corpora.Dictionary.load('.//Corpus//corpus.dict')
print dictionary

#Carica il modello LSI
lsi = models.LsiModel.load('.//Corpus//corpus_lsi.lsi')


f = codecs.open(".//Corpus//prova.txt", encoding='utf-8')
doc = f.read()
f.close()
doc = "cavani pippo pluto e paperino giocano a palla"

vec_bow = dictionary.doc2bow(doc.lower().split())

# convert the query to LSI space
vec_lsi = lsi[vec_bow]

index = similarities.docsim.MatrixSimilarity(lsi[corpus])
#index = similarities.docsim.MatrixSimilarity(lsi[corpus])

# perform a similarity query against the corpus
sims = index[vec_lsi]

#print (document_number, document_similarity) 2-tuples
lista = list(sims)
print sorted(lista)

#print numpy.mean([A[1] for A in sims])
print numpy.mean(sims)



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
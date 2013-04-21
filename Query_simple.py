'''
Created on 16/apr/2013
(Big luck!!)
Esegue query di somiglianza con un dizionario

@author: Francesco Collova
'''


from gensim import corpora
from gensim import models
from gensim import similarities



# Carica un corpus di documenti
corpus = corpora.MmCorpus('.//Corpus/corpus.mm')
print corpus

dictionary = corpora.Dictionary.load('.//Corpus/corpus.dict')
print dictionary

# build the index
index = similarities.Similarity('.//Corpus/', corpus, num_features=corpus.num_terms ) 

# get similarities between the query and all index documents
query = "partita calcio La Juventus vince con il Napoli"


vec_bow = dictionary.doc2bow(query.lower().split())
print vec_bow
similarities = index[vec_bow] 
print similarities



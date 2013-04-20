'''
Created on 16/apr/2013
(Big luck!!)
Esegue query di somiglianza con un dizionario

@author: Francesco Collova
'''

from gensim import corpora
from gensim import models
from gensim import similarities


corpus = corpora.MmCorpus('.//Corpus/corpus.mm')
print corpus

dictionary = corpora.Dictionary.load('.//Corpus//corpus.dict')
print dictionary



#lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=3)
lsi = models.LsiModel.load('.//Corpus//corpus_lsi.lsi')

doc ="Juventus"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow] # convert the query to LSI space
print vec_lsi
index = similarities.MatrixSimilarity(lsi[corpus])

sims = index[vec_lsi] # perform a similarity query against the corpus
print list(enumerate(sims)) # print (document_number, document_similarity) 2-tuples

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
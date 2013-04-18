from gensim import corpora
from gensim import models
from gensim import similarities



corpus = corpora.MmCorpus('corpus.mm')
print corpus

dictionary = corpora.Dictionary.load('corpus.dict')
print dictionary

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

index = similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=5)
print index

#lsi = models.LsiModel(corpus, id2word=dictionary.id2token, num_topics = 2)
#index = similarities.MatrixSimilarity(lsi[corpus])

doc = "Sport"
vec_bow = dictionary.doc2bow(doc.lower().split())
print vec_bow

vec_tfidf =tfidf[vec_bow]
print vec_tfidf

sims = index[vec_tfidf]

print list(enumerate(sims))


#print corpus.dictionary.token2id
#tfidf_trans = models.tfidfmodel.TfidfModel(corpus, id2word=corpora.dictionary)
#tfidf_corpus = corpora.Mncorpus(corpus=tfidf_trans[corpus], id2word=corpora.dictionary)
#lsi_trans = models.LsiModel(corpus=tfidf_corpus, id2word=corpora.dictionary, num_features=400)

#from gensim.similarities import Similarity
#index = Similarity(corpus=lsi_transformation[logent_transformation[corpus]], num_features=400, output_prefix="shard")
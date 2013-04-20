from gensim import corpora
from gensim import models
from gensim import similarities



# Carica un corpus di documenti
corpus = corpora.MmCorpus('.//Corpus/corpus.mm')
print corpus

dictionary = corpora.Dictionary.load('.//Corpus/corpus.dict')
print dictionary


lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=50)
lsi.save('.//Corpus/corpus_lsi.lsi')

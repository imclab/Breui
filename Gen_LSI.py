from gensim import corpora
from gensim import models
from gensim import similarities



# Carica un corpus di documenti
corpus = corpora.MmCorpus('.//Corpus/corpus.mm')
print corpus

dictionary = corpora.Dictionary.load('.//Corpus/corpus.dict')
print dictionary
print dictionary.token2id

# tfidf = models.TfidfModel(corpus)
# corpus_tfidf = tfidf[corpus]

lsi = models.LsiModel(corpus, num_topics=10, id2word = dictionary)
lsi.save('.//Corpus/corpus_lsi.lsi')

#Stampa i cluster dell'LSI
for topicN in range(lsi.num_topics):
    print 'topic %i: %s \n' % (topicN, lsi.print_topic(topicN))

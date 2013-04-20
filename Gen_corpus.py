'''
Created on 16/apr/2013
(Big luck!!)
Crea i dizionari a partire da un insiame di TXT

@author: Francesco Collova
'''





import os
from gensim import *

def iter_documents(top_directory):
    """Iterate over all documents, yielding a document (=list of utf8 tokens) at a time."""
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.txt'), files):
            document = open(os.path.join(root, file)).read() # read the entire document, as one big string
            yield utils.tokenize(document, lower=True) # or whatever tokenization suits you

class MyCorpus(object):
    def __init__(self, top_dir):
        self.top_dir = top_dir
        self.dictionary = corpora.Dictionary(iter_documents(top_dir))
        self.dictionary.filter_extremes(no_below=1, no_above=0.5, keep_n=3000) # check API docs for pruning params

    def __iter__(self):
        for tokens in iter_documents(self.top_dir):
            yield self.dictionary.doc2bow(tokens)

# create a corpus dictionary
corpus = MyCorpus('.//DataFile') 

for vector in corpus: # convert each document to a bag-of-word vector
    print vector
print list(corpus)

# Save Corpus
corpora.MmCorpus.serialize('.//Corpus//corpus.mm', corpus)
corpus.dictionary.save('.//Corpus/corpus.dict')
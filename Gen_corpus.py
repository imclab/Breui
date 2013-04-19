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
        self.dictionary.filter_extremes(no_below=1, no_above=0.5, keep_n=30000) # check API docs for pruning params

    def __iter__(self):
        for tokens in iter_documents(self.top_dir):
            yield self.dictionary.doc2bow(tokens)

corpus = MyCorpus('C://Documents and Settings//37509200//Desktop//NLTK-Python//Breui//DataFile') # create a dictionary
for vector in corpus: # convert each document to a bag-of-word vector
    print vector

print list(corpus)

# Save Corpus
corpora.MmCorpus.serialize('corpus.mm', corpus)
corpus.dictionary.save('corpus.dict')
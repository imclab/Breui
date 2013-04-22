'''
Created on 16/apr/2013
(Big luck!!)
Crea i dizionari a partire da un insiame di TXT

@author: Francesco Collova
'''
# -*- coding: utf-8 -*-




import os
from gensim import *
import codecs
import re
import string

#Carica le StopWord per l'italiano
f = codecs.open(".//stopword.txt", encoding='utf-8')
stopword = f.read().split()
f.close()
#print stopword

def rm_apostrofi(s):
    #Le assegnazioni fuori dalla funzione per velocizzare
    apostrofi = "l' un' all' dall' dell' d' sull' nell' quell' c' v'".split()
    pattern = '|'.join(map(re.escape, apostrofi))
    regstop = re.compile(pattern, re.UNICODE )
    return regstop.sub('', s)

#Rimuove la punteggiatura da un testo
regex = re.compile('[%s]' % re.escape(string.punctuation))
def remove_punct(s):
    return regex.sub('', s)

def iter_documents(top_directory):
    """Iterate over all documents, yielding a document (=list of utf8 tokens) at a time."""
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.txt'), files):
            document = codecs.open(os.path.join(root, file), encoding='utf-8').read() # read the entire document, as one big string
#            print document

            document = [word for word in document.lower().split() if word not in stopword]
            document = [rm_apostrofi(word) for word in document]
            document = [word for word in document if len(word) > 3 ]

#            Non funziona ad esempio con l'aereo si ha laereo
#            document = [remove_punct(word) for word in document]
            

#            print document
#            yield utils.tokenize(document, lower=True) # or whatever tokenization suits you
            yield document

class MyCorpus(object):
    def __init__(self, top_dir):
        self.top_dir = top_dir
        self.dictionary = corpora.Dictionary(iter_documents(top_dir))
        # check API docs for pruning params
        self.dictionary.filter_extremes(no_below=1, no_above=1, keep_n=100)


    def __iter__(self):
        for tokens in iter_documents(self.top_dir):
            yield self.dictionary.doc2bow(tokens)

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
print dictionary
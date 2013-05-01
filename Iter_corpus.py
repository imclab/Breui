# -*- coding: utf-8 -*-

'''
Created on 16/apr/2013
(Big luck!!)
Crea i dizionari a partire da un insiame di TXT

@author: Francesco Collova
'''


import os
from gensim import *
import codecs
import re
import string
from util import *

def iter_documents(top_directory):
    """Iterate over all documents, yielding a document (=list of utf8 tokens) at a time."""
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.txt'), files):
            document = codecs.open(os.path.join(root, file), encoding='utf-8').read() # read the entire document, as one big string
#            print document
            document = List_of_Word(document)
#             document = rm_apostrofi(document)
#             document = remove_punct(document)
#             document = [word for word in document.lower().split() if word not in stopword]
# #           document = [rm_apostrofi(word) for word in document]
#             document = [word for word in document if len(word) > 4 ]

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
        self.dictionary.filter_extremes(no_below=15, no_above=0.8, keep_n=100)

    def __iter__(self):
        for tokens in iter_documents(self.top_dir):
            yield self.dictionary.doc2bow(tokens)

import os
from gensim import *
import codecs
import re
import string


#Carica le StopWord per l'italiano
f = codecs.open(".\\stopword.txt", encoding='utf-8')
stopword = f.read().split()
f.close()
#print stopword

regex = re.compile('[%s]' % re.escape(string.punctuation))
#Rimuove la punteggiatura da un testo
def remove_punct(s):
    return regex.sub('', s)

#Rimuove le stopword anche in una sottostringa
stoppattern = '|'.join(map(re.escape, stopword))
regstop = re.compile(stoppattern, re.UNICODE )
def remove_stopword(s):
    return regstop.sub('', s)

stringa = "cinque case"
ss=remove_stopword(stringa)
print ss

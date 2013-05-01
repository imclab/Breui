import codecs
import re
import string


#Carica le StopWord per l'italiano
f = codecs.open(".\\stopword.txt", encoding='utf-8')
stopword = f.read().split()
f.close()
#print stopword

# regex = re.compile('[%s]' % re.escape(string.punctuation))
# #Rimuove la punteggiatura da un testo
# def remove_punct(s):
#     return regex.sub('', s)

# #Rimuove la punteggiatura da un testo
# regex = re.compile('[%s]' % re.escape(string.punctuation))
# def remove_punct(s):
#     return regex.sub('', s)

def remove_punct(s):
    pattern = '|'.join(map(re.escape, string.punctuation))
    regstop = re.compile(pattern, re.UNICODE )
    return regstop.sub(' ', s)



#Rimuove le stopword anche in una sottostringa

#Carica le StopWord per l'italiano
f = codecs.open(".//stopword.txt", encoding='utf-8')
stopword = f.read().split()
f.close()
stoppattern = '|'.join(map(re.escape, stopword))
regstop = re.compile(stoppattern, re.UNICODE )

def remove_stopword(s):
    return regstop.sub('', s)

def rm_apostrofi(s):
    #Le assegnazioni fuori dalla funzione per velocizzare
    apostrofi = "l' un' all' dall' dell' d' sull' nell' quell' c' v'".split()
    pattern = '|'.join(map(re.escape, apostrofi))
    regstop = re.compile(pattern, re.UNICODE )
    return regstop.sub('', s)



def vec_tuple2feature(tupleVect):
    featureVect = []
    for i in range(len(tupleVect)):
        Atuple = tupleVect[i]
        featureVect.append(Atuple[1])
    return(featureVect)

def doc_tuple2feature(tupleCorpus):
    featureDoc = []
    for x in tupleCorpus:
        tmp = []
        for i in range(len(x)):
            y = x[i]
            tmp.append(y[1])
        featureDoc.append(tmp)
    return featureDoc



def List_of_Word(document):
    document = rm_apostrofi(document)
    document = remove_punct(document)
    document = [word for word in document.lower().split() if word not in stopword]
#   document = [rm_apostrofi(word) for word in document]
    document = [word for word in document if len(word) > 4 ]
    return(document)

    
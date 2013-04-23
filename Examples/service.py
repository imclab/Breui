#http://www.scurtu.it/documentSimilarity.html

import urllib,urllib2
import json
API_URL="http://www.scurtu.it/apis/documentSimilarity"
inputDict={}
inputDict['doc1']='Document with some text'
inputDict['doc2']='Other document with some text'
params = urllib.urlencode(inputDict)    
f = urllib2.urlopen(API_URL, params)
response= f.read()
responseObject=json.loads(response)  
print responseObject
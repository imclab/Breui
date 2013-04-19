import nltk
import summarize
   
from urllib import urlopen
url = "http://www.repubblica.it/politica/2013/03/27/news/m5s_consultazioni_bersani_in_diretta_streaming-55441364/?ref=HREA-1"    
html = urlopen(url).read()    
raw = nltk.clean_html(html)  
print(raw)

ss = summarize.SimpleSummarizer()
##content = open('C:\\Documents and Settings\\37509200\\Desktop\\NLTK-Python\\summarize-master\\notizia.txt', 'r').read()
print(ss.summarize(raw, 2))

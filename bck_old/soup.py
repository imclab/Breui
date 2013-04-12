from urllib import urlopen
import re
from bs4 import  BeautifulSoup
import nltk
import summarize
from f_link import link

my_link='http://www.collova.it'

lista = link(my_link)

pattern='http://www\.repubblica\.it.*'

for item in lista:
    if not(re.match(pattern, item)):
        lista.remove(item)

print "\n".join(str(x) for x in lista)

for html_link in lista:
    news_link = urlopen(html_link).read()
    soup = BeautifulSoup(news_link)
    soup_text = soup.get_text()
    notizia = re.findall('inizio TESTO.*fine TESTO', soup_text)
    print(notizia)
    ss = summarize.SimpleSummarizer()
    raw_notizia = ' '.join(notizia)
    print(ss.summarize(raw_notizia, 2))



#texts = soup.findAll(text=True)
#
#def visible(element):
#    if element.parent.name in ['style', 'script', 'document', 'head', 'title']: return False
##    elif re.match('<!--.*-->', str(element)): return False
#    elif re.match('\n', str(element)): return False
#    else: return True
#visible_texts = filter(visible, texts)
#print(visible_texts)
#raw_text = ' '.join(visible_texts)
#raw_pulito = nltk.clean_html(raw_text)

'''
Created on 02/apr/2013

@author: Francesco Collova
'''
import summarize.summarize as riass
import urllib2
import nltk

import crawler_link
from bs4 import *
import re
from readability.readability import *

pagelist=['http://www.repubblica.it']
crawler = crawler_link.crawler('')
crawler.crawl(pagelist)
lista = crawler.link_list
ss = riass.SimpleSummarizer()

#for html_link in lista:
#    html = urllib2.urlopen(html_link).read()    
#    raw = nltk.clean_html(html) 
#    print(ss.summarize(raw, 2))

# filtra solo i link nel dominio
lista = [x for x in lista if u'www.repubblica.it'  in x]


for html_link in lista:
    file = urllib2.urlopen(html_link)
    news_page = file.read()
    news_soup = BeautifulSoup(news_page)
    news_title = news_soup.title.string
#    news_text = soup.get_text()
    goodnews = re.findall(u'inizio TESTO.*fine TESTO', news_page)
    if goodnews :
        output = Document(news_page, debug=False).summary().encode('ascii','ignore')
        raw = nltk.clean_html(output)
        #soupg = BeautifulSoup(output).get_text()
        print(news_title)
        print(ss.summarize(raw, 2))
        print("\n")


#   notizia = re.findall(u'inizio TESTO.*fine TESTO', soup_text)
#    if notizia :
#        notiziastr= re.sub(u'inizio TESTO', '', notizia[0])
#        notiziastr= re.sub(u'fine TESTO', '', notiziastr)
#        print(page_title)
#        print(ss.summarize(notiziastr, 2))
#        print("\n")


'''
Created on 12/apr/2013

Genera TXT di Articoli di tipo Sportivo da Repubblica

@author: Francesco Collova
'''


import urllib2
import nltk

import crawler_link
from bs4 import *
import re
from readability.readability import *



pagelist=['http://www.repubblica.it/sport/']
crawler = crawler_link.crawler('')
crawler.crawl(pagelist)
lista = crawler.link_list


# filtra solo i link nel dominio
lista = [x for x in lista if u'www.repubblica.it/sport'  in x]

counter=0
for html_link in lista:
    html_file = urllib2.urlopen(html_link)
    html = html_file.read()
    goodnews = re.findall(u'inizio TESTO.*fine TESTO', html)
    goodnews =True
    if goodnews :
        title = "C://Documents and Settings//37509200//Desktop//NLTK-Python//Breui//DataFile/"+"news" + str(counter) + ".txt"
        counter = counter +1

#        news_soup = BeautifulSoup(html)
#        news_text = news_soup.get_text()
#        #readability call
#        output = Document(html, debug=False).summary().encode('ascii','ignore')
#        soupg = BeautifulSoup(output).get_text()

        raw = nltk.clean_html(html)
        file = open(title, "w")
        try:
            file.write(raw) # Write a string to a file
        finally:
            file.close()

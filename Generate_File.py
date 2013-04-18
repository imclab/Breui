'''
Created on 12/apr/2013

Genera TXT di Articoli di tipo Sportivo da Repubblica

@author: Francesco Collova
'''


import urllib2
import nltk

import crawler_link
from bs4 import *
from bs4 import Comment
from readability.readability import *
import re
import string

def strbee(s, leader, trailer):
    end_of_leader = s.index(leader) + len(leader)
    start_of_trailer = s.index(trailer, end_of_leader)
    return s[end_of_leader:start_of_trailer]

pagelist=['http://www.repubblica.it/sport/']
#pagelist=['http://www.repubblica.it/sport/calcio/serie-a/roma/2013/04/16/news/roma_andreazzoli_lancia_destro_sar_la_sua_partita-56778823/']
crawler = crawler_link.crawler('')
crawler.crawl(pagelist)
lista = crawler.link_list


# filtra solo i link nel dominio
lista = [x for x in lista if u'www.repubblica.it/sport'  in x]
counter=0

for html_link in lista:
    news_page = urllib2.urlopen(html_link).read()
    soup = BeautifulSoup(news_page)
    page_title=soup.title.string
    soup_text = soup.get_text()
    notizia = re.findall(u'inizio TESTO.*fine TESTO', soup_text,re.UNICODE|re.DOTALL)
    if notizia :
        notiziastr= re.sub(u'inizio TESTO', '', notizia[0])
        notiziastr= re.sub(u'fine TESTO', '', notiziastr)
        title = "C://Documents and Settings//37509200//Desktop//NLTK-Python//Breui//DataFile/"+"news" + str(counter) + ".txt"
        counter = counter +1    
        file = open(title, "w")
        try:
            file.write(page_title)
            file.write(notiziastr) # Write a string to a file
        finally:
            file.close()



#    print soup_text
#   reg = re.compile(u'inizio TESTO.*fine  TESTO',re.UNICODE|re.DOTALL)
#    m = reg.search(soup_text)
    
#    print type(soup_text)    
#    A_soup_text= soup_text.encode('ascii', 'ignore')
#    print soup_text
#    notizia = re.search(ur'inizio TESTO(.*)fine  TESTO', soup_text, re.UNICODE|re.DOTALL)
#    print notizia.group(1)
#    AA=soup.find_all(text=re.compile("inizio TESTO"))
#    str_next_sib=u""
#    for comment in AA:
#        next_sib = comment.nextSibling
#        while not isinstance(next_sib, Comment) and \
#            not isinstance(next_sib, NavigableString) and next_sib:
#            # This prints each sibling while it isn't whitespace or another comment
#            # Append next_sib to a list, dictionary, etc, etc and
#            # do what you want with it
#            str_next_sib = str_next_sib + unicode(next_sib.text)
#            next_sib = next_sib.nextSibling
#    
#    comments = soup.findAll(text=lambda elm: isinstance(elm, Comment))


    
#    if m :
#        notiziastr=m.group(1)
#        notiziastr= re.sub(u'inizio TESTO', '', notizia[0])
#        notiziastr= re.sub(u'fine TESTO', '', notiziastr)
#        title = "C://Documents and Settings//37509200//Desktop//NLTK-Python//Breui//DataFile/"+"news" + str(counter) + ".txt"
#        counter = counter +1    
#        file = open(title, "w")
#        try:
#            file.write(notiziastr) # Write a string to a file
#        finally:
#            file.close()
            
            
            
                
    
#    html_file = urllib2.urlopen(html_link)
#    html_txt = html_file.read()
##    print html_txt
#    goodnews = re.findall('inizio TESTO', html_txt)
#    print goodnews
#    if  len(goodnews) > 0:
#        title = "C://Documents and Settings//37509200//Desktop//NLTK-Python//Breui//DataFile/"+"news" + str(counter) + ".txt"
#        counter = counter +1
#
##        news_soup = BeautifulSoup(html)
##        news_text = news_soup.get_text()
##        #readability call
##        output = Document(html, debug=False).summary().encode('ascii','ignore')
##        soupg = BeautifulSoup(output).get_text()
#
#        raw = nltk.clean_html(html_txt)
#        file = open(title, "w")
#        try:
#            file.write(raw) # Write a string to a file
#        finally:
#            file.close()

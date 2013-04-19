'''
Created on 28/mar/2013

@author: 37509200
'''
from urllib import urlopen
import re
from bs4 import  BeautifulSoup

def link(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html)
    link_list = []
    for href in soup.findAll('a'):
#      link_list.append(href['href'])
        link_list.append(href.get('href'))
    return(link_list)

#print(link('http://www.repubblica.it'))
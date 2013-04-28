# -*- coding: utf-8 -*-
'''
Created on 28/mar/2013
@author: F. Collova
'''
import re
import urllib2
from bs4 import *
from urlparse import urljoin
from time import gmtime, strftime
import pymongo

class crawler:
# Initialize the crawler with the name of database
    def __init__(self,db_name,saveDir):

        self.link_list = []
        self.counter=0
        self.saveDir = saveDir
        try:
            from pymongo import Connection
            self.connection = pymongo.Connection('mongodb://localhost:27017')
            self.database = self.connection[db_name]
        except:
            print('Error: Unable to connect to database.')
            self.connection = None

    def __del__(self):
        pass

    def dbcommit(self):
        self.connection.disconnect()
        

# Crawl in breadth first manner F.C. solo dei link nel dominio di Pages!!!

    def crawl(self,pages,depth=1):
        for i in range(depth):
            newpages=set( )
            for page in pages:
                try:
                    c=urllib2.urlopen(page)
                except:
                    print "Could not open %s" % page
                    continue
                soup=BeautifulSoup(c.read( ))
                self.addtoindex(page,soup)
                links=soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url=urljoin(page,link['href'])
                        if url.find("'")!=-1: continue
                        url=url.split('#')[0] # remove location portion
                        
                        #Attenzione fa il crawl solo dei link nel dominio
                        if (url[0:5]=='http:' and not self.isindexed(url)
                            and page in url):
                            newpages.add(url)
                            httpSoup, httpText = self.gettextonly(url)
                            if httpSoup :
                                notiziaStr = self.createFile(httpSoup,self.saveDir)
                            self.addlinkref(page,url,httpText,notiziaStr)
            self.dbcommit( )
        pages=newpages

# Auxilliary function for getting an entry id and adding
# it if it's not present    
    def getentryid(self,table,field,value,createnew=True):
        return None
# Index an individual page
    def addtoindex(self,url,soup):
        print 'Indexing %s' % url

# Extract the text from an HTML page (no tags)
    def gettextonly(self,url):
        print "Reading... %s" % url
        try:
            http_page = urllib2.urlopen(url).read()
            http_soup = BeautifulSoup(http_page)
            # Lo rende Unicode
            http_txt = http_soup.prettify()
            return http_soup, http_txt   
        except:
            print "Could not read %s" % url
            return None,None


# Separate the words by any non-whitespace character
    def separatewords(self,text):
        return None
# Return true if this url is already indexed
    def isindexed(self,url):
        ifurl = self.database.crawled.find({'urlTo': url})
        if ifurl.count()>0 : return True
        return False

#        if url in self.link_list : return True
#        return False


# Add a link between two pages
    def addlinkref(self,urlFrom,urlTo,httpText,notiziaStr):
        print 'Link %s'  % urlTo
        if self.connection is not None:
            GMTtime = gmtime()
            now = strftime("%Y-%m-%d %H:%M:%S", GMTtime)
            self.database.crawled.insert({'timestr': now,
                                          'counter': self.counter,
                                          'urlFrom': urlFrom,
                                          'urlTo': urlTo,
                                          'httpText': httpText,
                                          'notiziaStr' : notiziaStr})
            self.link_list.append(urlTo)

    def createFile(self,httpSoup,saveDir):
        notiziastr = "Nulla"
        title = ""
        soup_text = httpSoup.get_text()
        notizia = re.findall(u'inizio TESTO.*fine TESTO', soup_text,re.UNICODE|re.DOTALL)
        if notizia :
            try:
                title = httpSoup.find("title").string
            except:
                title=""
            notiziastr= re.sub(u'inizio TESTO', '', notizia[0])
            notiziastr= re.sub(u'fine TESTO', '', notiziastr)
            now = strftime("%Y-%m-%d %H%M%S", gmtime())
            filename = saveDir + "//News_" + now + str(self.counter) + ".txt"
            self.counter = self.counter +1    
            ff = open(filename, "w")
            try:
                ff.write(title)
                ff.write(notiziastr) # Write a string to a file
            finally:
                ff.close()
        return title + notiziastr
    
# Starting with a list of pages, do a breadth
# first search to the given depth, indexing pages
# Create the database tables
def createindextables(self):
    pass



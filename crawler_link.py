'''
Created on 28/mar/2013
@author: F. Collova
'''

import urllib2
from bs4 import *
from urlparse import urljoin

class crawler:
# Initialize the crawler with the name of database
    def __init__(self,dbname):
        self.link_list = []
    def __del__(self):
        pass
    def dbcommit(self):
        pass
# Crawl in breadth first manner F.C.

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
                        if url[0:4]=='http' and not self.isindexed(url):
                            newpages.add(url)
                            linkText=self.gettextonly(link)
                            self.addlinkref(page,url,linkText)
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
    def gettextonly(self,soup):
        return None
# Separate the words by any non-whitespace character
    def separatewords(self,text):
        return None
# Return true if this url is already indexed
    def isindexed(self,url):
        if url in self.link_list : return True
        return False
# Add a link between two pages
    def addlinkref(self,urlFrom,urlTo,linkText):
        print 'Link %s'  % urlTo
        self.link_list.append(urlTo)
# Starting with a list of pages, do a breadth
# first search to the given depth, indexing pages
# Create the database tables
def createindextables(self):
    pass



#pagelist=['http://www.repubblica.it']
#crawler = crawler('')
#crawler.crawl(pagelist)
#print crawler.link_list
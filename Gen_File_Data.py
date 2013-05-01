# Crawl link Store on DB and Create File

from Crawler_DB_File import *

pagelist=['http://www.repubblica.it/sport/calcio']
crawler = crawler('dblink',".//DataFile")
crawler.crawl(pagelist)
print crawler.link_list
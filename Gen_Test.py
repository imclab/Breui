# Crawl link Store on DB and Create File
from Crawler_DB_File import *

pagelist=['http://bit.ly/17YxEHr ']
crawler = crawler('dblinktest',".//TestFile")
crawler.crawl(pagelist)
print crawler.link_list
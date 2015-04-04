__author__ = 'Sravan'
import spiders.baseSpider as spider
import indexer.html_indexer as site_indexer

# CRAWLING
print 'Started Crawling..'
spider.crawl_seeds()
print 'Finished Crawling..'

# INDEXING
site_indexer.index_sites()
print 'Finished Indexing..'
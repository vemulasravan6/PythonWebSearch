__author__ = 'sravan'
import requests
from lxml import html
import ConfigParser
import json
import re
import time
import hashlib
from urlparse import urlparse
import os

def http_download(url):
    try:
        page = requests.get(url)
        return page.text.encode('utf-8')
    except:
        exception_flag = True
        print 'url:'+url
        pass

def create_dir_structure(spider,base_dir):
    #creates crawl_alerts/spider dir if not exists
    if os.path.exists(base_dir)==False:
        os.makedirs(base_dir)
        base_dir=base_dir+'/'+spider
        os.makedirs(base_dir)
        print 'Created..'+base_dir
    else:
        #checks for spider dir,creates 1 if not exists
        base_dir=base_dir+'/'+spider
        if os.path.exists(base_dir)==False:
            os.makedirs(base_dir)
    return base_dir

def crawl(url):
    visited = []
    home_page = http_download(url)
    url_parse_obj = urlparse(url)
    dump_dir_name = url_parse_obj.netloc.split('.')[1]
    #loading into DOM Tree
    tree = html.fromstring(home_page)
    #Extracting urls from home page
    urls = tree.xpath('.//a/@href')
    dump_dir = create_dir_structure(dump_dir_name,'html_dumps')
    #recursively spidering all the urls
    for url in urls:
        if url not in visited:
            print 'Fetching..'+url
            page_content = http_download(url)
            if page_content:
                file_name_with_url = url.replace("/","\\")
                with open(dump_dir+'/'+file_name_with_url, 'w') as f:
                    f.write(page_content)
                    visited.append(url)
    return

def get_site_urls(seed_file):
    site_urls = []
    try:
        with open(seed_file) as seed_file_contents:
            for seed_url in seed_file_contents.readlines():
                site_urls.append(seed_url.rstrip())
    except:
        pass
    return site_urls

def crawl_seeds():
    for seed in get_site_urls('sites_to_crawl.txt'):
        crawl(seed)
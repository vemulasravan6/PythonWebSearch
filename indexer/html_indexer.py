__author__ = 'Sravan'
import os
import re
from bs4 import BeautifulSoup
import json
import sys

def index_sites():
    INDEX_FILE = 'search_index.json'
    #LOADING THE EXISTING INDEX FILE IF EXISTS
    DATA_STORE = {}
    if os.path.exists(INDEX_FILE):
        try:
            with open(INDEX_FILE) as json_file:
                DATA_STORE = json.load(json_file)
        except:
            DATA_STORE = {}
            e_msg = os.getcwd()
            e_msg = e_msg+'\n\n\n=====INVALID INDEX FILE , SKIPPING TO LOAD EXISTING INDEX\n\n\n'
            print e_msg

    base_dir = "html_dumps"
    for directory in os.listdir(base_dir):
        #print  directory
        for html_file in os.listdir(base_dir+'/'+directory):
            url = html_file.replace("\\","/")
            fo = open(base_dir+'/'+directory+'/'+html_file, "r+")
            file_str = fo.read()
            file_str = BeautifulSoup(file_str).get_text()
            #extracting words
            keywords = re.findall("\w+",file_str)
            for keyword in keywords:
                if keyword not in DATA_STORE:
                    tmp_list = []
                    tmp_list.append(url)
                    DATA_STORE[keyword]=tmp_list
                else:
                    existing_list = DATA_STORE[keyword]
                    if url not in existing_list:
                        existing_list.append(url)
    #UPDATING INDEX
    j = json.dumps(DATA_STORE, indent=4)
    f = open(INDEX_FILE, 'w')
    print >> f, j
    f.close()
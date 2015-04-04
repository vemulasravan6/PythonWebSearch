__author__ = 'Sravan'
__mail__ = 'vemulasravan6@gmail.com'
import os
import json
import sys

#loading index
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

search_key=''
try:
    search_key = sys.argv[1]
except:
    print '\nPls input ur key as argument. Happy Searching..\n'
    print 'Ex:- python search.py hotel  # to search for hotel keyword \n'
    sys.exit()

if len(DATA_STORE)>0:
    print '\n=============Searching for : '+search_key+'=============\n'
    if search_key in DATA_STORE:
        for search_result in DATA_STORE[search_key]:
            print search_result
    else:
        print '\n'+search_key+' : Not Found, Try other key'+'\n'
else:
    print 'Key not found'
# PythonWebSearch
Simple and basic search engine in python for small scale websites
______________________________________________________________________

Welcome to the PythonWebSearch wiki!

Developed in/for Linux distributions

SYS Requirements:

Ubuntu

Python installation

sudo apt-get install python3
Pip installation # to install python packages

easy_install pip
Installing lxml

apt-get install libxml2-dev libxslt1-dev python-dev
apt-get install python-lxml
Installing required modules

pip install requests

-----

To run this tool
====================

Navigate to crawlers directory

open sites_to_crawl.txt and update website list to crawl, i've added 2 sites

Crawling & indexing

/var/bin/python crawl.py

You shud see the following msg on the console, upon successful completion

Finished Crawling.. Finished Indexing..

Raw dumps will get stored in html_dumps dir

indexed data can be found in search_index.json

To search for hotel keyword across websites

python search.py hotel

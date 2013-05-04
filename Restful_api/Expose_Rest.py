# -*- coding: utf-8 -*-
'''
Created on 04/mag/2013
@author: F. Collova
'''

from rfc3987 import parse
import json
import bottle
from bottle import route, run, request, abort
import urllib2
from bs4 import *
import nltk

# from pymongo import Connection

from urlparse import urlparse
# urlparse('http://----')
# # returns: ParseResult(scheme='http', netloc='----', path='', params='', query='', fragment='')

def is_valid_url(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)


def Http2Text(self,httpSoup):
    notiziastr = "Nulla"
    title = ""
    soup_text = httpSoup.get_text()
    try:
        title = httpSoup.find("title").string
    except:
        title=""
#         notiziastr= re.sub(u'inizio TESTO', '', notizia[0])
#         notiziastr= re.sub(u'fine TESTO', '', notiziastr)
#         now = strftime("%Y-%m-%d %H%M%S", gmtime())
    return title + " " + soup_text





# connection = Connection('localhost', 27017)
# db = connection.mydatabase
# @route('/documents', method='PUT')
# def put_document():
#     data = request.body.readline()
#     if not data:
#         abort(400, 'No data received')
#     entity = json.loads(data)
#     if not entity.has_key('_id'):
#         abort(400, 'No _id specified')
#     try:
#         db['documents'].save(entity)
#     except ValidationError as ve:
#         abort(400, str(ve))
#
#usage: http://localhost:8080/link/?url=http://www.google.com

1 
@route('/link/', method='GET')
def get_link():

#     entity = db['documents'].find_one({'_id':id})
#     if is_valid_url(vlink)

    url = request.GET.get("url")
#    test = parse(url, rule='IRI') non funziona ????????
    test = is_valid_url(url)
    if not test:
        abort(404, 'Invalid url parameter')
    try:
        http_page = urllib2.urlopen(url).read()
        http_soup = BeautifulSoup(http_page)
        # Lo rende Unicode
        http_txt = http_soup.prettify()
        raw = nltk.clean_html(http_txt)
        soup_txt = http_soup.get_text()
        return '<<<------------------------ WELCOME to Breui Restful Api ---------------------->>>' + raw   
    except:
        return "Could not read %s" % url


# = parse('http://fdasdf/fss', rule='IRI')
run(host='localhost', port=8080)
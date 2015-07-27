# -*- coding: utf-8 -*-
"""
Setting file used for the natural language processing module (nlp.py)
"""
__title__ = 'wikipy'
__author__ = 'Colby Brown'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015, Colby Brown'

import logging
import os

from http.cookiejar import CookieJar as cj

log = logging.getLogger(__name__)

PARENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

STOPWORDS_DIR = os.path.join(PARENT_DIRECTORY, 'resources/text')

# NLP stopwords
NLP_STOPWORDS_EN = os.path.join(PARENT_DIRECTORY, 'resources/misc/stopwords-nlp-en.txt')

DATA_DIRECTORY = '.wikipy_scraper'

TOP_DIRECTORY = os.path.join(os.path.expanduser("~"), DATA_DIRECTORY)
if not os.path.exists(TOP_DIRECTORY):
    os.mkdir(TOP_DIRECTORY)

# Error log
LOGFILE = os.path.join(TOP_DIRECTORY, 'wikipy_errors_%s.log')
MONITOR_LOGFILE = os.path.join(
    TOP_DIRECTORY, 'wikipy_monitors_%s.log')

# Memo directory (same for all concur crawlers)
MEMO_FILE = 'memo'
MEMO_DIR = os.path.join(TOP_DIRECTORY, MEMO_FILE)

if not os.path.exists(MEMO_DIR):
    os.mkdir(MEMO_DIR)

# Category and feed cache
CF_CACHE_DIRECTORY = 'feed_category_cache'
ANCHOR_DIRECTORY = os.path.join(TOP_DIRECTORY, CF_CACHE_DIRECTORY)

if not os.path.exists(ANCHOR_DIRECTORY):
    os.mkdir(ANCHOR_DIRECTORY)

TRENDING_URL = 'http://www.google.com/trends/hottrends/atom/feed?pn=p1'


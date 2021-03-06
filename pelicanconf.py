#!/gnu/store/72rsajyxlf5qsq9wjabmalz64nyl4kdb-python-wrapper-3.8.2/bin/python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Morgan Lemmer-Webber'
SITENAME = 'Morgan\'s Crafty Corner'
# SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
## LINKS = ()

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = "blog/{slug}/"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

STATIC_PATHS  = [
    "images",
    "dissertation"
]

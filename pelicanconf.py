#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'rainy'
SITENAME = u'雨生'
SITEURL = 'http://0.0.0.0:8080'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh-CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_MAX_ITEMS = 20

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

# MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
DEFAULT_PAGINATION = 10
THEME = "themes/MD"
THEME = "themes/prose"

DEFAULT_DATE_FORMAT = '%Y-%m-%d'


ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

TEMPLATE_PAGES = {"/Users/rainy/Projects/Blog/pelican.rainy.im/themes/prose/templates/about.html": 'about/index.html'}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
# PLUGIN_PATH = "plugins"
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["neighbors"]
STATIC_PATHS = ["images"]

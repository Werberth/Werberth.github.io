#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Werberth Vinícius'
SITENAME = u'Werberth Vinicius'
AUTHOR_EMAIL = u'werberthvinicius@gmail.com'
SITEURL = 'https://werberth.github.io'

SIDE_BAR_IMG = 'images/banner.jpg'
COVER_IMG_URL = SITEURL + '/' + SIDE_BAR_IMG

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images']
THEME = 'theme'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter-square', 'http://twitter.com/Werberthgomes'),
          ('github', 'https://github.com/Werberth'),
          ('facebook', 'https://www.facebook.com/werberthg'))

PLUGIN_PATHS = [
    'pelican-plugins'
]

PLUGINS = [
    'gravatar',
    'sitemap',
    'disqus_static'
]

DISQUS_SITENAME = 'werberthvinicius'


DEFAULT_PAGINATION = 10

GOOGLE_ANALYTICS = 'UA-104570304-1'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'pages': 0.8,
        'indexes': 0.5
    },
    'exclude': ['tag/'],
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly',
        'pages': 'monthly'
    }
}

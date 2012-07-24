#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Andrea Crotti"
SITENAME = u"Coding blog"
SITEURL = 'http://andreacrotti.github.com/personal-blog/'

TIMEZONE = 'Europe/London'

DEFAULT_LANG='English'

# Blogroll
LINKS =  (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
    # ('Jinja2', 'http://jinja.pocoo.org'),
    # ('You can modify those links in your config file', '#')
)

# Social widget
SOCIAL = (
          ('You can add links in your config file', '#'),
         )

PDF_GENERATOR = False

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

DEFAULT_PAGINATION = 5

GITHUB_URL = 'http://github.com/andreacrotti/'

DISQUS_SITENAME = "andreacrotti"

SOCIAL = (('twitter', 'http://twitter.com/andreacrotti/'),
          ('github', 'http://github.com/andreacrotti/'),)



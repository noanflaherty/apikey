#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'apikey',
    'version': '1.0.0',
    'description': 'Simple script to change colors of parts in a document',
    'long_description': open('README.md').read(),
    'author': 'Noa Flaherty',
    'url': 'https://github.com/onshape/apikey/tree/master/python',
    'license': open('LICENSE').read(),
    'packages': [
        'apikey'
    ],
    'classifiers': [
        'Programming Language :: Python',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
}

setup(**config)

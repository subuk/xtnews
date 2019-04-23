# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys
sys.path.insert(0, 'src')

requires = [
    'pyramid',
    'WebError',
    'pymongo',
    'wtforms',
    'python-dateutil',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'pyramid_jinja2',
]

setup(
    name='xtnews',
    author='Matvey Kruglov',
    author_email='kubus@openpz.org',
    version='0.1',
    packages=['xtnews'],
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'xtnews-initdb = xtnews.scripts.initdb:main',
        ],
        'paste.app_factory': [
            'main = xtnews:main'
        ]
    },
)

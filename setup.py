# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys
sys.path.insert(0, 'src')

requires = [
    'webob',
    'python-dateutil',
]

setup(
    name='xtnews',
    author='Matvey Kruglov',
    author_email='kubus@openpz.org',
    version=__import__('xtnews').__version__,
    packages=['xtnews'],
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'xtnews = xtnews.main:run',
        ]
    },
)

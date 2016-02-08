#!/usr/bin/env python3

from distutils.core import setup
import os

setup(
    name = 'pypcappy',
    packages = ['pypcappy', 'pypcappy.blocks'], 
    version = '0.0.1',
    description = 'Pure Python3 PcapNg reader',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    author = 'Guy Taylor',
    author_email = 'thebigguy.co.uk@gmail.com',
    url = 'https://github.com/TheBiggerGuy/pypcappy',
    keywords = ['pcap'], 
    license = 'MIT',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],  
)

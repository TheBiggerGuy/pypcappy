#!/usr/bin/env python3

import sys
if sys.version_info < (3,):
    print('ERROR: Only Python 3 is supported')
    sys.exit(-1)


# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path, system
import re


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open('pypcappy/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'pypcappy',
    version = version,
    description = 'Pure Python3 PcapNg reader',
    long_description = long_description,
    author = 'Guy Taylor',
    author_email = 'thebigguy.co.uk@gmail.com',
    url = 'https://github.com/TheBiggerGuy/pypcappy',
    packages = find_packages(exclude=['docs', 'tests']),
    package_data={'': ['LICENSE', 'README.md']},
    install_requires=[],
    keywords = ['pcap'], 
    license = 'MIT',
    classifiers = (
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
)

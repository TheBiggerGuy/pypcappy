#!/usr/bin/env python3

import sys
if sys.version_info < (3,):
    print('ERROR: Only Python 3 is supported')
    sys.exit(-1)


# To use a consistent encoding
from codecs import open
from os import path, system
import re
import sys

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


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
    zip_safe=False,
    install_requires=[],
    tests_require=['pytest'],
    cmdclass = {'test': PyTest},
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

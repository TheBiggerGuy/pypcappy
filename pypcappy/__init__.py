#!/usr/bin/env python3

import sys
if sys.version_info < (3,):
    print('ERROR: Only Python 3 is supported')
    sys.exit(-1)

__title__ = 'pypcappy'
__version__ = '0.0.7'
__author__ = 'Guy Taylor'

from .pcapNgFile import PcapNgFile

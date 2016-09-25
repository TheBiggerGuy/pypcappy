PyPcapPy
========
**A Pure Python3 PcapNg reader**

[![Build Status](https://travis-ci.org/TheBiggerGuy/pypcappy.svg?branch=master)](https://travis-ci.org/TheBiggerGuy/pypcappy)
[![Coverage Status](https://coveralls.io/repos/github/TheBiggerGuy/pypcappy/badge.svg?branch=master)](https://coveralls.io/github/TheBiggerGuy/pypcappy?branch=master)
[![Requirements Status](https://requires.io/github/TheBiggerGuy/pypcappy/requirements.svg?branch=master)](https://requires.io/github/TheBiggerGuy/pypcappy/requirements/?branch=master)
[![PyPI version](https://badge.fury.io/py/pypcappy.svg)](https://badge.fury.io/py/pypcappy)

Use
===
```python
with PcapNgFile('file_name.pcapng.gz') as pcap_file:
  for packet in pcap_file.packets:
    print(packet)
```

Why not pypcap or pypcapfile?
=============================
* Pure python
 * Will work on CPython, PyPy, Jpython or whatever
* Python 3
 * No legacy packet data as strings
* PcapNG
 * Only support for the new *next gen* format
* Gzip
 * Build in support for both *.pcapng and *.pcapng.gz files
 
Downloads
=========
* Source tar.gz via [GitHub](https://github.com/TheBiggerGuy/pypcappy/releases/latest)
* [PyPI](https://pypi.python.org/pypi/pypcappy)

Links
=====
* http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.html

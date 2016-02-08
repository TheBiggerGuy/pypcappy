PyPcapPy
========
**A Pure Python3 PcapNg reader**

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
** Will work on CPython, PyPy, Jpython or whatever
* Python 3
** No legacy packet data as strings
* PcapNG
** Only support for the new *next gen* format
* Gzip
** Build in support for both *.pcapng and *.pcapng.gz files
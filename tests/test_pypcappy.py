#!/usr/bin/env python3

import pytest

from pypcappy import PcapNgFile

def test_missingfile(tmpdir):
    tmpdir = str(tmpdir)
    with pytest.raises(FileNotFoundError):
        with PcapNgFile(tmpdir + '/missing.pcapng') as pcap:
            pass

def test_emptyfile(tmpdir):
    tmpdir = str(tmpdir)
    open(tmpdir + '/empty.pcapng', 'a').close()
    with PcapNgFile(tmpdir + '/empty.pcapng') as pcap:
        for block in pcap.blocks:
            assert False # should never get here
#!/usr/bin/env python3

import gzip

class Packet(object):
    """docstring for Packet"""
    def __init__(self, byteorder, data):
        super(Packet, self).__init__()
        self.byteorder = byteorder
        self.data = data

    def __str__(self):
        return 'Packet of ' + str(len(self.data)) + ' bytes'
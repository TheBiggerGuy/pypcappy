#!/usr/bin/env python3

class AbstractBlock(object):
    TYPE_IDS = []

    """docstring for PcapNgBlock"""
    def __init__(self, byteorder, block_type, data, skip=False):
        self.byteorder = byteorder
        if block_type not in self.TYPE_IDS and not skip:
            raise Exception('Invalid TypeID for ' + str(self.block_type_name()) + ': ' + str(block_type))
        self.block_type = block_type
        self.data = data

    @property
    def block_type_name(self):
        raise NotImplementedError()

    def __str__(self):
        return 'PcapNgBlock: ' + str(self.block_type_name())
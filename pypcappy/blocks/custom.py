#!/usr/bin/env python3

from . import AbstractBlock

class CustomBlock(AbstractBlock):
    TYPE_IDS = [0x00000BAD, 0x40000BAD]

    def __init__(byteorder, self, block_type, data):
        super(self).__init__(byteorder, block_type, data)

    def block_type_name(self):
        return 'Custom Block (CB)'
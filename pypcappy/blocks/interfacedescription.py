#!/usr/bin/env python3

from . import AbstractBlock

class InterfaceDescriptionBlock(AbstractBlock):
    TYPE_IDS = [0x00000001]

    def __init__(self, byteorder, block_type, data):
        super().__init__(byteorder, block_type, data)

    def block_type_name(self):
        return 'Interface Description Block (IDB)'
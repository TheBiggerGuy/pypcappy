#!/usr/bin/env python3

from . import AbstractBlock

class SectionHeaderBlock(AbstractBlock):
    TYPE_IDS = [0x0A0D0D0A]

    def __init__(self, byteorder, block_type, data):
        super().__init__(byteorder, block_type, data)

    def block_type_name(self):
        return 'Section Header Block (SHB)'
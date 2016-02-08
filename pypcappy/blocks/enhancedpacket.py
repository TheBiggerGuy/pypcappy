#!/usr/bin/env python3

from ..packet import Packet
from . import AbstractBlock

class EnhancedPacketBlock(AbstractBlock):
    TYPE_IDS = [0x00000006]

    def __init__(self, byteorder, block_type, data):
        super().__init__(byteorder, block_type, data)

    def block_type_name(self):
        return 'Enhanced Packet Block (EPB)'

    @property
    def capture_len(self):
        return int.from_bytes(self.data[20:25], byteorder=self.byteorder, signed=False)

    @property
    def original_len(self):
        return int.from_bytes(self.data[20:25], byteorder=self.byteorder, signed=False) 

    @property
    def packet(self):
        return Packet(self.byteorder, self.data[28:28 + 1 + self.capture_len])
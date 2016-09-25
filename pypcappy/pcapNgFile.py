#!/usr/bin/env python3

import gzip

from .blocks import BLOCK_TYPES
from .blocks.enhancedpacket import EnhancedPacketBlock

class BlockInterator(object):
    def __init__(self, file):
        self._file = file
        self._current_byteorder = None

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._file.peek(1)) == 0:
            raise StopIteration

        # set or maintain the correct byteorder
        is_section_header_block = self._peek(4) == bytes([0x0A, 0x0D, 0x0D, 0x0A])
        if self._current_byteorder == None and not is_section_header_block:
            raise Exception('Invalid file: No SectionHeaderBlock (' + str(self._peek(4)) + ')')
        if is_section_header_block:
            self._peek_and_set_current_byteorder()

        # read the block in full
        block_type = int.from_bytes(self._file.read(4), byteorder=self._current_byteorder, signed=False)
        block_len = int.from_bytes(self._file.read(4), byteorder=self._current_byteorder, signed=False)
        block_data  = self._file.read(block_len - 4 - 4 - 4)
        block_len_tail = int.from_bytes(self._file.read(4), byteorder=self._current_byteorder, signed=False)
        if block_len != block_len_tail:
            raise Exception('Invalid block')

        return BLOCK_TYPES[block_type](self._current_byteorder, block_type, block_data)

    def _peek_and_set_current_byteorder(self):
        byteorder_magic = self._peek(8 + 4)[0x08:0x0C]
        byteorder_little = int.from_bytes(byteorder_magic, byteorder='little', signed=False)
        byteorder_big = int.from_bytes(byteorder_magic, byteorder='big', signed=False)
        if byteorder_little == 0x1A2B3C4D:
            self._current_byteorder = 'little'
        elif byteorder_big == 0x1A2B3C4D:
            self._current_byteorder = 'big'
        else:
            raise Exception('Invalid SectionHeaderBlock Byte-order Magic')

    def _peek(self, size):
        return self._file.peek(size)[:size]

class PacketInterator(object):
    def __init__(self, blocks):
        self._packets = (block.packet for block in blocks if isinstance(block, EnhancedPacketBlock))

    def __iter__(self):
        return self._packets


class PcapNgFile(object):
    """Wrapper around a sinlge pcap-ng file"""
    def __init__(self, file):
        super(PcapNgFile, self).__init__()
        if isinstance(file, str):
            file = open(file, 'rb')
        if file.peek(2)[:2] == bytes([0x1F, 0x8B]):
            file = gzip.open(file, mode='rb')
        self._file = file
    
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_val, trace):
        self._file.close()

    @property
    def blocks(self):
        return BlockInterator(self._file)

    @property
    def packets(self):
        return PacketInterator(self.blocks)

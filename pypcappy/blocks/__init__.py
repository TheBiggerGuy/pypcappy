#!/usr/bin/env python3

from importlib import import_module

from .abstract import AbstractBlock

"""
from .sectionHeaderBlock import SectionHeaderBlock
from .customBlock import CustomBlock
from .interfaceDescriptionBlock import InterfaceDescriptionBlock
from .enhancedPacketBlock import EnhancedPacketBlock

BLOCK_TYPES = {
    0x0A0D0D0A: SectionHeaderBlock,
    0x00000001: InterfaceDescriptionBlock,
    0x00000002: ToDoBlock, #'!OBSOLETE! Packet Block',
    0x00000003: ToDoBlock, #'Simple Packet Block (SPB)',
    0x00000004: ToDoBlock, #'Name Resolution Block (NRB)',
    0x00000005: ToDoBlock, #'Interface Statistics Block (ISB)',
    0x00000006: EnhancedPacketBlock,
    0x00000BAD: CustomBlock,
    0x40000BAD: CustomBlock
}
"""


class ToDoBlock(AbstractBlock):
    TYPE_IDS = []

    def __init__(self, byteorder, block_type, data):
        super().__init__(byteorder, block_type, data, skip=True)

    def block_type_name(self):
        return 'TODO Block'

class BlockLibary(object):
	def __init__(self):
		self.blocks = {}

	def add(self, type_id, block):
		if type_id < 0 or type_id > 0xFFFFFFFF:
			raise Exception('Invalid block type id: ' + str(type_id))
		self.blocks[type_id] = block

	def __getitem__(self, type_id):
		if type_id < 0 or type_id > 0xFFFFFFFF:
			raise Exception('Invalid block type id: ' + str(type_id))
		return self.blocks.get(type_id, ToDoBlock)

BLOCK_TYPES = BlockLibary()

for block_name in ['Abstract', 'SectionHeader', 'Custom', 'InterfaceDescription', 'EnhancedPacket']:
	module = import_module('.' + block_name.lower(), package='pypcappy.blocks')
	block = getattr(module, block_name + 'Block')
	for type_id in block.TYPE_IDS:
		BLOCK_TYPES.add(type_id, block)

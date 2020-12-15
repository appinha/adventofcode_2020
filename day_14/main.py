# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
import re
import itertools as it
from collections import defaultdict


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	return raw_input


class MemValue:
	''' Class for value to be put in memory (Part One). '''
	def __init__(self, value, mask):
		self.value = value
		self.mask_value = self.apply_mask(value, mask)

	def __str__(self):
		return "value = %i, mask_value = %i" % (self.value, self.mask_value)

	def __repr__(self):
		return self.__str__()

	def apply_mask(self, value, mask):
		''' Apply bitmask to value. Return masked binary converted to int.'''
		value_bin = '{0:036b}'.format(value)
		mask_bin = ''
		for i, b in enumerate(mask):
			mask_bin += b if b in ['1', '0'] else value_bin[i]
		return int(mask_bin, 2)


def ft_part1(data):
	''' Put values into dictionary with memory addresses as keys. Return the sum
		of masked values in dictionary. '''
	dc_memvals = defaultdict(MemValue)
	for line in data:
		if line[:4] == 'mask':
			mask = line.replace('mask = ', '')
		if line[:3] == 'mem':
			mem, value = line.split('] = ')
			dc_memvals[mem.replace('mem[', '')] = MemValue(int(value), mask)
	return sum(dc_memvals[k].mask_value for k in dc_memvals)


def apply_mask_mem(mem, mask):
	''' Apply bitmask to memory address. Return a list of masked addresses. '''
	mem_bin = '{0:036b}'.format(mem)
	mask_bin_X = ''
	for i, b in enumerate(mask):
		mask_bin_X += b if b in ['X', '1'] else mem_bin[i]
	ls_floating_bins = list(it.product([0, 1], repeat=mask.count('X')))
	ls_mask_bin = []
	for fl_bin in ls_floating_bins:
		mask_bin = ''
		j = 0
		for i, b in enumerate(mask_bin_X):
			if b == 'X':
				mask_bin += str(fl_bin[j])
				j += 1
			else:
				mask_bin += mask_bin_X[i]
		ls_mask_bin.append(mask_bin)
	return [int(m, 2) for m in ls_mask_bin]


def ft_part2(data):
	''' Put values into dictionary with masked memory addresses as keys. Return
		the sum of values in dictionary. '''
	dc_memvals = defaultdict(int)
	for line in data:
		if line[:4] == 'mask':
			mask = line.replace('mask = ', '')
		if line[:3] == 'mem':
			mem, value = line.split('] = ')
			ls_mask_mem = apply_mask_mem(int(mem.replace('mem[', '')), mask)
			for m in ls_mask_mem:
				dc_memvals[m] = int(value)
	return sum(dc_memvals[k] for k in dc_memvals)


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

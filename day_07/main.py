import sys
sys.path.append('../common_core')
from common_core import core

import re


input_file = 'input.txt'


def ft_input_parser(raw_input):

	def parse_rules(line):
		'''Convert given line to dictionary key of bag rules.'''

		item_regex = re.compile(r'^(\d+) ([a-z\s]+) bags?\.?$')

		def get_contents(line):
			qty, item = item_regex.match(line).groups()
			return (int(qty), item)

		container, contents = line.split(" bags contain ")
		if contents == "no other bags.":
			return container, []
		return container, [get_contents(item) for item in contents.split(', ')]

	return dict([parse_rules(line) for line in raw_input])


def ft_part1(data):

	def rec_find_bag(data, needle):
		'''
			Recursively check if given bag (needle) is in given dictionary of
			bag rules (data).
		'''
		ls_keys = [key for key in data for value in data[key] if value[1] == needle]
		for valid_key in ls_keys:
			ls_keys += rec_find_bag(data, valid_key)
			ls_keys = list(set(ls_keys))
		return ls_keys

	return len(rec_find_bag(data, 'shiny gold'))


def ft_part2(data):

	def rec_count(data, needle):
		'''
			Recursively count how many bags are inside the given bag (needle).
		'''
		return 1 + sum(qty * rec_count(data, item) for qty, item in data[needle])

	return rec_count(data, 'shiny gold') - 1


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)


# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core

# Import requirements
import re


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	'''Convert given input (list of strings) to dictionary of bag rules.'''

	def parse_line(line):
		item_regex = re.compile(r'^(\d+) ([a-z\s]+) bags?\.?$')

		def get_contents(line):
			qty, item = item_regex.match(line).groups()
			return (int(qty), item)

		container, contents = line.split(" bags contain ")
		if contents == "no other bags.":
			return container, []
		return container, [get_contents(item) for item in contents.split(', ')]

	return dict([parse_line(line) for line in raw_input])


def ft_part1(data):

	def rec_find_bag(data, needle):
		''' Recursively check if given bag (needle) is in given dictionary of
			bag rules (data). '''
		ls_keys = [key for key in data for value in data[key] if value[1] == needle]
		for valid_key in ls_keys:
			ls_keys += rec_find_bag(data, valid_key)
			ls_keys = list(set(ls_keys))
		return ls_keys

	return len(rec_find_bag(data, 'shiny gold'))


def ft_part2(data):

	def rec_count(data, needle):
		''' Recursively count bags inside given bag (needle). '''
		return 1 + sum(qty * rec_count(data, item) for qty, item in data[needle])

	return rec_count(data, 'shiny gold') - 1


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2)

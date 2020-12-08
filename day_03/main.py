# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
from numpy import prod


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	return raw_input


def count_trees(lines, right, down):
	'''
		Count how many trees were encountered in map with given slope.
	'''
	count = 0
	x = 0
	for y in range(down, len(lines), down):
		x += right
		if x >= len(lines[y]):
			x = x - len(lines[y])
		if lines[y][x] == '#':
			count += 1
	return count


def ft_part1(data):
	return count_trees(data, 3, 1)


def ft_part2(data):
	inputs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
	return prod([count_trees(data, i[0], i[1]) for i in inputs])


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

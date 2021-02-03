# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core

# Import requirements
import itertools as it
import numpy as np


def ft_input_parser(raw_input):
	''' Convert input into list of numbers (integers). '''
	return [int(line) for line in raw_input]


def ft_find_nbrs(ls_nbrs, qty):
	''' Find numbers in given list (ls_nbrs) whose sum is equal to 2020. '''
	for nbrs in it.combinations(ls_nbrs, qty):
		if sum(nbrs) == 2020:
			return nbrs


def ft_part1(data):
	''' Get the product of the 2 numbers found. '''
	return np.prod(ft_find_nbrs(data, 2))


def ft_part2(data):
	''' Get the product of the 3 numbers found. '''
	return np.prod(ft_find_nbrs(data, 3))


if __name__ == '__main__':
	ft_core(sys.argv[1], ft_input_parser, ft_part1, ft_part2)

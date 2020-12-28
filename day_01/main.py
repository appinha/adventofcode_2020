# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core

# Import requirements
from numpy import prod


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	return [int(line) for line in raw_input]


def find_nbrs(data, qty):
	# Loop through list of numbers n times for combinatorial analysis
	for i in range(len(data)):
		for j in range(i + 1, len(data)):
			# PART ONE - Check if sum of two numbers is equal to 2020
			if (qty == 2):
				if (data[i] + data[j] == 2020):
					return [data[i], data[j]]
			# PART TWO - Check if sum of three numbers is equal to 2020
			elif (qty == 3):
				for k in range(j + 1, len(data)):
					if (data[i] + data[j] + data[k] == 2020):
						return [data[i], data[j], data[k]]


def ft_part1(data):
	return prod(find_nbrs(data, 2))


def ft_part2(data):
	return prod(find_nbrs(data, 3))


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2)

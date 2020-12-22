# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
import re


input_file = sys.argv[1]


class Nbr(int):
	'''
	Class for storing numbers from math expressions.
	The subtraction method will perform a multiplication instead, so it has same
	precedence as addition (Part One).
	'''
	def __add__(self, x):
		return Nbr(int(self) + x)

	def __sub__(self, x):
		return Nbr(int(self) * x)

	def __mul__(self, x):
		return Nbr(int(self) + x)


def ft_input_parser(raw_input):
	return raw_input


def ft_eval_expr(data, part):
	'''
	This function applies regex to each line (string) of the input, converting
	digits to a Nbr object and replacing '*' with '-' (in order to perform a
	multiplication with same precedence as addition) and (for Part Two) '+' with
	'*' (in order to perform addition with more precedence than multiplication),
	thus applying eval(). It returns the sum of all eval() results.
	'''
	def regex(line):
		if part == 1:
			return re.sub(r'(\d+)', r'Nbr(\1)', line).replace('*', '-')
		if part == 2:
			return re.sub(r'(\d+)', r'Nbr(\1)', line\
					).replace('*', '-').replace('+', '*')

	return sum(eval(regex(line)) for line in data)


def ft_part1(data):
	return ft_eval_expr(data, 1)


def ft_part2(data):
	return ft_eval_expr(data, 2)


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

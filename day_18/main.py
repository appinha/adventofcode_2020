# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core

# Import requirements
import re


input_file = sys.argv[1]


class Nbr(int):
	'''
	Class for storing numbers from math expressions.
	The subtraction method will perform a multiplication instead, in order to
	perform multiplications with same precedence as additions (Part One).
	The multiplication method will perform an addition instead, in order to
	perform additions with more precedence than multiplications.
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
	This function applies regex to each line (string) of the input, convertingr
	digits to Nbr objects, thus replacing '*' with '-' (in order to perform
	multiplications with same precedence as additions), and (for Part Two)
	'+' with '*' (in order to perform additions with more precedence than
	multiplications), thus applying eval() to the resulting expression.
	It returns the sum of all eval() results (for each line in the input).
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
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2)

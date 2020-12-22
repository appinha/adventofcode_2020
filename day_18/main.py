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


def ft_input_parser(raw_input):
	return raw_input


def ft_eval_expr(data):
	'''
	This function applies regex to each line (string) of the input, converting
	digits to a Nbr object and replacing '*' with '-' (in order to perform a
	multiplication with same precedence as addition), thus applying eval(). It
	returns the sum of all eval() results.
	'''
	return sum(eval(re.sub(r'(\d+)', r'Nbr(\1)', line).replace('*', '-')) \
			for line in data)


def ft_part1(data):
	return ft_eval_expr(data)


#def ft_part2(data):
#	return


if __name__ == '__main__':
	#core(input_file, ft_input_parser, ft_part1, ft_part2, delimiter='\n\n')
	core(input_file, ft_input_parser, ft_part1, False)

# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
import re


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	'''
		Split with regex each input line's values - two integers, a character
		and a string - into sublists.
	'''
	return [re.split('-| |: ', line) for line in raw_input]


# Values' indexes
IND_1 = 0
IND_2 = 1
CHAR = 2
STR = 3


def ft_part1(data):

	def check(pwd, ind_1, ind_2):
		''' Check if given password is valid according to password policy. '''
		count = pwd[STR].count(pwd[CHAR])
		if ind_1 <= count <= ind_2:
			return True
		return False

	return len([pwd for pwd in data \
				if check(pwd, int(pwd[IND_1]), int(pwd[IND_2]))])


def ft_part2(data):

	def count_checks(line, ind_1, ind_2):
		''' Check if given password is valid according to password policy. '''

		def check(line, ind):
			if ind < len(line[STR]):
				if line[CHAR] == line[STR][ind]:
					return 1
			return 0

		if (check(line, ind_1) + check(line, ind_2)) == 1:
			return True
		return False

	return len([pwd for pwd in data \
				if count_checks(pwd, int(pwd[IND_1]) - 1, int(pwd[IND_2]) - 1)])


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

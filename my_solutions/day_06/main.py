# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	return raw_input


def get_ls_uniques(block):
	''' Get list of unique values (characters). '''
	return list(set(block.replace('\n', '')))


def ft_part1(data):
	''' Sum the counts of unique values in groups' answers. '''
	return sum(len(get_ls_uniques(block)) for block in data)


def ft_part2(data):
	''' Sum the counts of answers present in all group members answers. '''
	def count(block):
		nbr_members = block.count('\n') + 1
		ls_uniques = get_ls_uniques(block)
		return sum(1 for c in ls_uniques if block.count(c) == nbr_members)

	return sum(count(block) for block in data)


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2, delimiter='\n\n')

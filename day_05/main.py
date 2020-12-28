# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	return raw_input


def bpcode2seatID(bpcode):
	'''
		Convert boarding pass code to seat ID.
	'''
	def bin2int(code, char):
		''' Convert binary pattern to integer. '''
		loc = 0
		exp = len(code) - 1
		for c in code:
			if c == char:
				loc += 2 ** exp
			exp -= 1
		return loc

	return 8 * bin2int(bpcode[0:7], 'B') + bin2int(bpcode[7:], 'R')


def get_seatID(data):
	return [bpcode2seatID(line) for line in data]


def ft_part1(data):
	return max(get_seatID(data))


def ft_part2(data):
	ls_seatID = get_seatID(data)
	range_seatID = [*range(min(ls_seatID), max(ls_seatID) + 1)]
	for seat in range_seatID:
		if seat not in ls_seatID:
			return seat


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2)


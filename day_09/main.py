# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	return [int(line) for line in raw_input]


def find_invalid_nbr(data):
	''' Find invalid number according to XMAS encription. '''
	def find_sum(data, start, end):
		for i in range(start, end):
			for j in range(start + 1, end):
				if (data[i] + data[j] == data[end]):
					return True
		return False

	preamble = int(sys.argv[2])
	for n in range(preamble, len(data)):
		if find_sum(data, n - preamble, n) == False:
			return data[n]


def find_weakness(data):
	invalid_nbr = find_invalid_nbr(data)
	for i in range(len(data)):
		for j in range(i + 1, len(data)):
			seq_sum = sum(data[i:j])
			if seq_sum > invalid_nbr:
				break
			elif seq_sum == invalid_nbr:
				return data[i:j]


def ft_part1(data):
	return find_invalid_nbr(data)


def ft_part2(data):
	seq = find_weakness(data)
	return min(seq) + max(seq)


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2)

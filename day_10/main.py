# Import common core
import sys
sys.path.append('../common_core')
from common_core import core


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	data = [int(line) for line in raw_input]
	return [0] + sorted(data) + [max(data) + 3]


def ft_part1(data):
	diffs = [0, 0]
	for i in range(1, len(data)):
		diff = data[i] - data[i - 1]
		if diff == 1:
			diffs[0] += 1
		if diff == 3:
			diffs[1] += 1
	return diffs[0] * diffs[1]


def ft_part2(data):
	subgroups = ''.join(str(data[i + 1] - data[i]) for i in range(len(data) - 1)).split('3')
	deltas = [len(ones) for ones in subgroups if len(ones) > 1]
	sums = [sum(1 for n in deltas if n == i) for i in range(2, 5)]
	return (2 ** sums[0]) * (4 ** sums[1]) * (7 ** sums[2])


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

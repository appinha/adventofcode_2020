# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core

# Import requirements
from numpy import prod


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	'''
		This function parses the input, converting the given list of strings
		(lines from input file) to a list of integers.
	'''
	data = [int(line) for line in raw_input]
	return [0] + sorted(data) + [max(data) + 3]


def ft_part1(data):
	'''
		This function counts how many deltas between numbers ("jolt difference")
		of given sequence are equal to 1 and 3. The return is the product of
		these counts.
	'''
	diffs = [0, 0]
	for i in range(1, len(data)):
		diff = data[i] - data[i - 1]
		if diff == 1:
			diffs[0] += 1
		if diff == 3:
			diffs[1] += 1
	print(diffs)
	return diffs[0] * diffs[1]


def ft_part2(data):
	'''
		This function creates a string with the deltas between numbers of given
		sequence ("131113113111133"), then splits it on the 3s. The resulting
		list of subgroups of ones ([[1], [111], [11], [1111], []]) is pruned and
		converted to a list of subgroups' quantity of 1s ([3, 2, 4]), with
		length < 2 subgroups being discarded because they don't allow for any
		combinations other than the subgroup itself. The quantity of 1s is thus
		substituted for the number of possible combinations in each subgroup
		([4, 2, 7]). The return is the combination of all subgroup combinations,
		i.e. the product of these numbers.
	'''
	subgroups = ''.join(str(data[i + 1] - data[i]) for i in range(len(data) - 1)).split('3')
	qty_ones = [len(ones) for ones in subgroups if len(ones) > 1]
	cmbs = [2, 4, 7]
	return prod([cmbs[n - 2] for n in qty_ones])


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2)

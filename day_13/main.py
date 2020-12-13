# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
from numpy import prod


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	return raw_input


def ft_part1(data):
	''' Find ID of earliest bus and waiting time according to timestamp. '''
	timestamp = int(data[0])
	ls_bus = [int(bus) for bus in data[1].split(',') if bus != 'x']

	ls_divs = [(timestamp / bus) % 1 for bus in ls_bus]
	earliest_bus = ls_bus[ls_divs.index(max(ls_divs))]
	waiting = ((int(timestamp / earliest_bus) + 1) * earliest_bus) - timestamp
	return earliest_bus * waiting


def ft_part2(data):
	''' Find earliest timestamp where all bus cycles match.'''
	ls_inc, ls_bus = zip(*[(i, int(bus)) \
					for i, bus in enumerate(data[1].split(',')) if bus != 'x'])
	# Start time at first bus ID
	t = ls_bus[0]
	# Loop through bus list from second bus ID to last
	for i in range(1, len(ls_bus)):
		# While ((time + bus' initial time increment) % bus ID) isn't null
		while (t + ls_inc[i]) % ls_bus[i]:
			# Increment time with product of bus IDs already cycled
			t += prod(ls_bus[:i])
	return t


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

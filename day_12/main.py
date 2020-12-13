# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
from collections import deque


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	return raw_input


directions = ['N', 'E', 'S', 'W']


def change_dir(curr_dir, rot, deg):
	new_dir = deque(directions)
	r = -1 if rot == 'R' else 1
	new_dir.rotate(4 - directions.index(curr_dir) + r * int(deg / 90))
	return new_dir[0]


def ft_part1(data):
	dc_dirs = dict.fromkeys(directions, [])
	curr_dir = 'E'
	for line in data:
		if line[0] == 'R' or line[0] == 'L':
			curr_dir = change_dir(curr_dir, line[0], int(line[1:]))
		if line[0] == 'N' or (line[0] == 'F' and curr_dir == 'N'):
			dc_dirs['N'] = dc_dirs.get('N') + [int(line[1:])]
		if line[0] == 'E' or (line[0] == 'F' and curr_dir == 'E'):
			dc_dirs['E'] = dc_dirs.get('E') + [int(line[1:])]
		if line[0] == 'S' or (line[0] == 'F' and curr_dir == 'S'):
			dc_dirs['S'] = dc_dirs.get('S') + [int(line[1:])]
		if line[0] == 'W' or (line[0] == 'F' and curr_dir == 'W'):
			dc_dirs['W'] = dc_dirs.get('W') + [int(line[1:])]
	return abs(sum(dc_dirs['N']) - sum(dc_dirs['S'])) + \
			abs(sum(dc_dirs['E']) - sum(dc_dirs['W']))


#def ft_part2(data):

#	return


if __name__ == '__main__':
	#core(input_file, ft_input_parser, ft_part1, ft_part2, delimiter='\n\n')
	core(input_file, ft_input_parser, ft_part1, False)

# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
from collections import defaultdict, deque


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	''' Convert input to a list of [instruction (string), value (int)]. '''
	return [[line[0], int(line[1:])] for line in raw_input]


directions = ['N', 'E', 'S', 'W']


def rotate_dir(dirs, curr_dir, clockwise, deg):
	''' Rotate current direction according to clockwise and rotation degree. '''
	new_dir = deque(dirs)
	r = -1 if clockwise == 'R' else 1
	new_dir.rotate(4 - dirs.index(curr_dir) + r * int(deg / 90))
	return new_dir[0]


def calc_dist(dc_dirs):
	''' Calculate ship's *Manhattan distance* (sum of the absolute values of its
		east/west position and its north/south position). '''
	return abs(sum(dc_dirs['E']) - sum(dc_dirs['W'])) + \
			abs(sum(dc_dirs['N']) - sum(dc_dirs['S']))


def ft_part1(data):
	'''
		This function loops through given instructions (data), populating a
		dictionary with direction offsets. The return is the ship's *Manhattan
		distance*, calculated from collected direction offsets.
	'''
	dc_dirs = defaultdict(list)
	curr_dir = 'E'
	for instr, value in data:
		if instr in directions:
			dc_dirs[instr].append(value)
		if instr == 'R' or instr == 'L':
			curr_dir = rotate_dir(directions, curr_dir, instr, value)
		if instr == 'F':
			dc_dirs[curr_dir].append(value)
	return calc_dist(dc_dirs)


def ft_part2(data):
	'''
		This function loops through given instructions (data), populating a
		dictionary with direction offsets. The return is the ship's *Manhattan
		distance*, calculated from collected direction offsets.
	'''
	def rotate_wp(curr_wp, instr, value):
		''' Rotate current waypoint according to given instruction. '''
		wp_dirs = ['NE', 'SE', 'SW', 'NW']
		new_wp = [rotate_dir(wp_dirs, curr_wp[0], instr, value)]
		diff = wp_dirs.index(new_wp[0]) - wp_dirs.index(curr_wp[0])
		return new_wp + [v for v in curr_wp[1:]] if abs(diff) % 2 == 0 \
			else new_wp + [v for v in reversed(curr_wp[1:])]

	def update_wp(waypoint, instr, value):
		''' Update waypoint according to given instruction. '''
		if instr == 'N' or instr == 'S':
			waypoint[1] += value if waypoint[0][0] == instr else -value
		if instr == 'E' or instr == 'W':
			waypoint[2] += value if waypoint[0][1] == instr else -value

	dc_dirs = defaultdict(list)
	waypoint = ['NE', 1, 10]
	for instr, value in data:
		if instr in directions:
			update_wp(waypoint, instr, value)
		if instr == 'R' or instr == 'L':
			waypoint = rotate_wp(waypoint, instr, value)
		if instr == 'F':
			dc_dirs[waypoint[0][0]].append(value * waypoint[1])
			dc_dirs[waypoint[0][1]].append(value * waypoint[2])
	return calc_dist(dc_dirs)


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

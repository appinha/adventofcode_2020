# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
from collections import defaultdict, deque


input_file = sys.argv[1]


directions = ['N', 'E', 'S', 'W']

class Waypoint:
	''' Class for waypoint. '''
	def __init__(self, dir_NS, value_NS, dir_EW, value_EW):
		self.dir_NS = dir_NS
		self.value_NS = value_NS
		self.dir_EW = dir_EW
		self.value_EW = value_EW

	def __str__(self):
		return "Waypoint: %s%i %s%i" % \
			(self.dir_NS, self.value_NS, self.dir_EW, self.value_EW)

	def update(self, instr, value):
		''' Update waypoint according to given instruction. '''
		if instr in ['N', 'S']:
			self.value_NS += value if self.dir_NS == instr else -value
		if instr in ['E', 'W']:
			self.value_EW += value if self.dir_EW == instr else -value

	def rotate(self, instr, value):
		''' Rotate current waypoint according to given instruction. '''
		wp_dirs = ['NE', 'SE', 'SW', 'NW']
		new_dir = rotate_dir(wp_dirs, (self.dir_NS + self.dir_EW), instr, value)
		diff = wp_dirs.index(new_dir) - wp_dirs.index((self.dir_NS + self.dir_EW))
		self.dir_NS = new_dir[0]
		self.dir_EW = new_dir[1]
		if abs(diff) % 2 == 1:
			self.value_NS, self.value_EW = self.value_EW, self.value_NS


def ft_input_parser(raw_input):
	''' Convert input to a list of [instruction (string), value (int)]. '''
	return [[line[0], int(line[1:])] for line in raw_input]


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
	dc_dirs = defaultdict(list)
	wp = Waypoint('N', 1, 'E', 10)
	for instr, value in data:
		if instr in directions:
			wp.update(instr, value)
		if instr == 'R' or instr == 'L':
			wp.rotate(instr, value)
		if instr == 'F':
			dc_dirs[wp.dir_NS].append(value * wp.value_NS)
			dc_dirs[wp.dir_EW].append(value * wp.value_EW)
	return calc_dist(dc_dirs)


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

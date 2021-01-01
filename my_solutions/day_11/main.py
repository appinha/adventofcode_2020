# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core

# Import requirements
import copy
import numpy as np


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	'''
		This function parses the input, converting the given list of strings
		(lines from input file), which represents a seat map in form of a grid,
		to a dictionary (function's return) with keys for storing seat positions
		(tuples) according to seat's state:
			- 'u': seats in unpermanent state;
			- '.': floor (a permanent state);
			- '#': permanentely occupied seats;
			- 'L': permanentely empty seats;
	'''
	data = dict.fromkeys(['u', '.', '#'], [])
	for row in range(len(raw_input)):
		for col, value in enumerate(raw_input[row]):
			if value == '.':
				data['.'] = data.get('.') + [(row, col)]
			if raw_input[row][col] == 'L':
				data['u'] = data.get('u') + [(row, col)]
	data['map'] = np.matrix([list(raw_input[row]) for row in range(len(raw_input))])
	return data


ROW = 0
COL = 1


def get_all_adjacents(data, map_size, in_sight=False):
	''' Create a dictionary of adjacent seats (value) for all seats (keys). '''
	def check_in_map(pos):
		''' Check if position is inside seat map. '''
		return True if 0 <= pos[ROW] < map_size[ROW] and \
						0 <= pos[COL] < map_size[COL] else False

	def get_imed_adj(pos, ls_rel_a):
		''' Get imediatly adjacent seats (part 1 adjacent rule). '''
		ls_adj = [(a[ROW] + pos[ROW], a[COL] + pos[COL]) for a in ls_rel_a]
		return [a for a in ls_adj if check_in_map(a)]

	def get_in_sight(data, pos, ls_rel_a):
		''' Get seats in sight (part 2 adjacent rule). '''
		i = 1
		ls_adj = []
		while ls_rel_a:
			ls_to_remove = []
			for rel_a in ls_rel_a:
				abs_a = (i * rel_a[ROW] + pos[ROW], i * rel_a[COL] + pos[COL])
				if check_in_map(abs_a) == False:
					ls_to_remove.append(rel_a)
				elif abs_a not in data['.']:
					ls_adj.append(abs_a)
					ls_to_remove.append(rel_a)
			for to_remove in ls_to_remove:
				ls_rel_a.remove(to_remove)
			i += 1
		return ls_adj

	ls_rel_a = [(r, c) for r in range(-1, 2) for c in range(-1, 2) if not (r == 0 and c == 0)]
	dc_adj = {}
	for pos in data['u']:
		dc_adj[pos] = get_in_sight(data, pos, ls_rel_a[:]) if in_sight \
						else get_imed_adj(pos, ls_rel_a[:])
	return dc_adj


def get_occ(data, adj, pos, part):
	''' Get list of permanently occupied seats. '''
	count = 0
	for a in adj:
		count += 1 if a not in data['u'] else 0
	count += (8 - len(adj)) if len(adj) < 8 else 0
	if part == 1:
		return True if count > 4 else False
	if part == 2:
		return True if count > 3 else False


def get_emp(data, adj, pos):
	''' Get list of permanently empty seats. '''
	for a in adj:
		if a in data['#']:
			return True
	return False


def update_state(data, ls_pos, state):
	''' Update seat states from unpermanent to permanent. '''
	for pos in ls_pos:
		data['u'].remove(pos)
		if state == '#':
			data[state] = data.get(state) + [pos]
			data['map'][pos] = state


def seating_game(data, part):
	'''
		This function loops through seating rules, changing seat states from
		unpermanent to permanent until no unpermanently stated seat remains.
		The return is the quantity of permanently occupied seats.
	'''
	map_size = (data['map'].shape[ROW], data['map'].shape[COL])
	if part == 1:
		print("• Map size:", map_size[0], "x", map_size[1], \
				"=", map_size[0] * map_size[1], "positions")
		print("• Total seats:", len(data['u']))
		dc_adj = get_all_adjacents(data, map_size)
	if part == 2:
		dc_adj = get_all_adjacents(data, map_size, in_sight=True)

	i = 0
	while data['u']:
		occ = [pos for pos in data['u'] if get_occ(data, dc_adj[pos], pos, part)]
		update_state(data, occ, '#')
		emp = [pos for pos in data['u'] if get_emp(data, dc_adj[pos], pos)]
		update_state(data, emp, 'L')
		i += 1
	print("• Total interactions:", i)

	return len(data['#'])


def ft_part1(data):
	return seating_game(copy.deepcopy(data), 1)


def ft_part2(data):
	return seating_game(copy.deepcopy(data), 2)


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2)

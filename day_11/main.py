# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
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


def get_map_size(data):
	''' Get map size: (total rows, total cols). '''
	return (data['map'].shape[ROW], data['map'].shape[COL])


def get_adjacents(ls_pos, map_size):
	''' Create a dictionary of adjacent seats (value) for all seats (keys). '''
	rel_adj = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
	dc_adj = {}
	for pos in ls_pos:
		tmp = [(a[ROW] + pos[ROW], a[COL] + pos[COL]) for a in rel_adj]
		dc_adj[pos] = [t for t in tmp if 0 <= t[ROW] < map_size[ROW] and \
										0 <= t[COL] < map_size[COL]]
	return dc_adj


def get_occ(data, adj, pos):
	''' Get list of permanently occupied seats. '''
	count = 0
	for a in adj:
		count += 1 if a not in data['u'] else 0
	count += (8 - len(adj)) if len(adj) < 8 else 0
	return True if count > 4 else False


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


def seating_game_1(data):
	'''
		This function loops through seating rules, changing seat states from
		unpermanent to permanent until no unpermanently stated seat remains.
		The return is the quantity of permanently occupied seats.
	'''
	map_size = get_map_size(data)
	dc_adj = get_adjacents(data['u'], map_size)
	print("• Map size:", map_size[0], "x", map_size[1], \
			"=", map_size[0] * map_size[1], "positions")
	print("• Total seats:", len(data['u']))

	i = 0
	while data['u']:
		occ = [pos for pos in data['u'] if get_occ(data, dc_adj[pos], pos)]
		update_state(data, occ, '#')
		emp = [pos for pos in data['u'] if get_emp(data, dc_adj[pos], pos)]
		update_state(data, emp, 'L')
		i += 1
	print("• Total interactions:", i, "\n")

	return len(data['#'])


def ft_part1(data):
	return seating_game_1(data)


#def ft_part2(data):

#	return


if __name__ == '__main__':
	#core(input_file, ft_input_parser, ft_part1, ft_part2, delimiter='\n\n')
	core(input_file, ft_input_parser, ft_part1, False)

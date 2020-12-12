# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
import numpy as np


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	data = dict.fromkeys(['o', '.', '#'], [])
	data['map'] = np.matrix([list(raw_input[row]) for row in range(len(raw_input))])
	for row in range(len(raw_input)):
		for col in range(len(raw_input[row])):
			if raw_input[row][col] == '.':
				data['.'] = data.get('.') + [(row, col)]
			if raw_input[row][col] == 'L':
				data['o'] = data.get('o') + [(row, col)]
	return data


def print_dict(data):
	for key in data:
		print("•", key, "-", data[key])


ROW = 0
COL = 1

def change_key(data, ls_pos, new):
	for pos in ls_pos:
		data['o'].remove(pos)
		if new == '#':
			data[new] = data.get(new) + [pos]
			data['map'][pos] = new


def get_adj(data, pos):
	map_len = data['map'].shape[COL]
	adj = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]
	for a in adj:
		a[ROW] += pos[ROW]
		a[COL] += pos[COL]
	return [tuple(a) for a in adj if 0 <= a[ROW] < map_len and 0 <= a[COL] < map_len]


def get_occ(data, pos):
	adj = get_adj(data, pos)
	count = 0
	for a in adj:
		if a not in data['o']:
			count += 1
	if len(adj) < 8:
		count += 8 - len(adj)
	if count > 4:
		return True
	return False


def get_emp(data, pos):
	adj = get_adj(data, pos)
	for a in adj:
		if a in data['#']:
			return True
	return False


def ft_part1(data):
	print("Total seats:", len(data['o']))

	i = 0
	while data['o']:
		occ = [pos for pos in data['o'] if get_occ(data, pos)]
		change_key(data, occ, '#')
		emp = [pos for pos in data['o'] if get_emp(data, pos)]
		change_key(data, emp, 'L')
		i += 1
	print("inter:", i)

	#print_dict(data)
	return len(data['#'])


#def ft_part2(data):

#	return


if __name__ == '__main__':
	#core(input_file, ft_input_parser, ft_part1, ft_part2, delimiter='\n\n')
	core(input_file, ft_input_parser, ft_part1, False)

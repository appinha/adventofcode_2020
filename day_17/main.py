# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
import itertools as it
from collections import defaultdict


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	return raw_input


def get_ina_adj(exts):
	''' Get list of new layer of inactive neighbors. '''
	ls_diff = [-1, +1]
	lim = [n + ls_diff[i % 2] for i, n in enumerate(exts)]
	ls_ranges_out = [range(lim[i], lim[i + 1]) for i in range(0, len(lim), 2)]
	ls_ranges_in = [range(exts[i], exts[i + 1]) for i in range(0, len(exts), 2)]
	outer = list(it.product(*ls_ranges_out))
	inner = list(it.product(*ls_ranges_in))
	return [pos for pos in outer if pos not in inner]


def input2dict(raw_input, n_dimen):
	'''
		This function parses the input, converting the given list of strings
		(lines from the input file), which represents a 2D map of Conway Cubes,
		to a dictionary (function's return) with keys for storing cube positions
		(tuples) according to cube's state:
			- '.': cube is inactive;
			- '#': cube is active.
		Other required complementary information are stored as follows:
			- 'rel_adj': list of relative adjacent coordinates;
			- 'exts': current extents of infinite grid.
	'''
	extra_pos = tuple(it.chain.from_iterable(it.repeat([0], n_dimen - 2)))
	extra_exts = list(it.chain.from_iterable(it.repeat([0, 1], n_dimen - 2)))
	rel_adj = list(it.product([-1, 0, 1], repeat=n_dimen))
	rel_adj.remove((0, 0) + extra_pos)
	data = defaultdict(list)
	data['rel_adj'] = rel_adj
	for x, line in enumerate(raw_input):
		for y, value in enumerate(line):
			if value == '.':
				data['.'].append((x, y) + extra_pos)
			if value == '#':
				data['#'].append((x, y) + extra_pos)
	data['exts'] = [0, x + 1, 0, y + 1] + extra_exts
	data['.'] += get_ina_adj(data['exts'])
	return data


def get_all_adjacents(data, dc_adj):
	''' Create a dictionary of neighbors (adjacent cubes) for all cubes. '''
	def get_abs_adj(pos, adj):
		''' Get absolute coordinates of neighbor (adj) for given cube (pos). '''
		return tuple([pos[i] + adj[i] for i in range(len(pos))])

	def get_adjacents(ls_pos):
		''' Get neighbors for cubes in list (ls_pos)'''
		for pos in ls_pos:
			if pos not in ls_existing_pos:
				dc_adj[pos] += [get_abs_adj(pos, adj) for adj in data['rel_adj'][:]]

	ls_existing_pos = list(dc_adj)
	for ls_pos in [data['#'], data['.']]:
		get_adjacents(ls_pos)
	return dc_adj


def count_actives(adj, data):
	''' Count how many active cubes are in given list of adjacent cubes. '''
	count = 0
	for a in adj:
		count += 1 if a in data['#'] else 0
	return count


def update_state(ls_pos, orig, dest):
	''' Update cube states (orig -> dest). '''
	for pos in ls_pos:
		orig.remove(pos)
		dest.append(pos)


def boot_up(data):
	'''
		This function loops through state rules, changing cube states from
		active to inactive and vice-versa, for six cycles. The return is the
		quantity of remaining active cubes after the six-cycle boot.
	'''
	dc_adj = defaultdict(list)
	ls_inc = [-1, +1]
	i = 0
	while i < 6:
		dc_adj = get_all_adjacents(data, dc_adj)
		act2ina = [pos for pos in data['#'] \
					if count_actives(dc_adj[pos], data) not in [2, 3]]
		ina2act = [pos for pos in data['.'] \
					if count_actives(dc_adj[pos], data) == 3]
		update_state(act2ina, data['#'], data['.'])
		update_state(ina2act, data['.'], data['#'])
		data['exts'] = [n + ls_inc[i % 2] for i, n in enumerate(data['exts'])]
		data['.'] += get_ina_adj(data['exts'])
		i += 1
	return len(data['#'])


def ft_part1(data):
	return boot_up(input2dict(data, 3))


def ft_part2(data):
	return boot_up(input2dict(data, 4))


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
import copy
from collections import defaultdict


input_file = sys.argv[1]


def get_ina_adj(exts):
	''' Get list of new layer of inactive neighbors. '''
	def gen_pos(xl, xh, yl, yh, zl, zh):
		''' Generate coordinates within given low and high range values. '''
		return [(x, y, z) for x in range(xl, xh) for y in range(yl, yh) \
				for z in range(zl, zh)]

	nxl = exts[0] - 1 # xl
	nxh = exts[1] + 2 # xh
	nyl = exts[2] - 1 # yl
	nyh = exts[3] + 2 # yh
	nzl = exts[4] - 1 # zl
	nzh = exts[5] + 1 # zh
	ls_new = gen_pos(nxl, nxh, nyl, nyh, nzl, nzl + 1) + \
				gen_pos(nxl, nxh, nyl, nyh, nzh, nzh + 1) + \
				gen_pos(nxl, nxh, nyl, nyl + 1, nzl + 1, nzh) + \
				gen_pos(nxl, nxh, nyh - 1, nyh, nzl + 1, nzh) + \
				gen_pos(nxl, nxl + 1, nyl + 1, nyh - 1, nzl + 1, nzh) + \
				gen_pos(nxh - 1, nxh, nyl + 1, nyh - 1, nzl + 1, nzh)
	return ls_new


def ft_input_parser(raw_input):
	data = defaultdict(list)
	for x, line in enumerate(raw_input):
		for y, value in enumerate(line):
			if value == '.':
				data['.'].append((x, y, 0))
			if value == '#':
				data['#'].append((x, y, 0))
	data['exts'] = [0, x, 0, y, 0, 0]
	data['.'] += get_ina_adj(data['exts'])
	return data


XX = 0
YY = 1
ZZ = 2

ls_rel_adj = [(x, y, z) for x in range(-1, 2) for y in range(-1, 2) \
			for z in range(-1, 2) if not (x == 0 and y == 0 and z == 0)]

def get_all_adjacents(data, dc_adj):
	''' Create a dictionary of neighbors (adjacent cubes) for all cubes. '''
	def get_adj(ls_pos):
		''' Get neighbors for cubes in list (ls_pos)'''
		for pos in ls_pos:
			if pos not in ls_existing_pos:
				dc_adj[pos] += [(a[XX] + pos[XX], a[YY] + pos[YY], \
									a[ZZ] + pos[ZZ]) \
									for a in ls_rel_adj[:]]

	ls_existing_pos = list(dc_adj)
	for ls_pos in [data['#'], data['.']]:
		get_adj(ls_pos)
	return dc_adj


def count_actives(adj, data):
	count = 0
	for a in adj:
		count += 1 if a in data['#'] else 0
	return count


def update_state(ls_pos, orig, dest):
	for pos in ls_pos:
		orig.remove(pos)
		dest.append(pos)


def print_data_info(data, dc_adj):
	print("DATA INFO")
	qty_act = len(data['#'])
	qty_ina = len(data['.'])
	print("• qty '#':", qty_act)
	print("• qty '.':", qty_ina)
	print("• qty all:", qty_act + qty_ina)
	print("• qty adj:", len(dc_adj))
	print("• extents:", data['exts'])
	print()


def boot_up(data):
	dc_adj = defaultdict(list)
	ls_inc = [-1, +1]
	i = 0
	while i < 6:
		dc_adj = get_all_adjacents(data, dc_adj)
		# print_data_info(data, dc_adj)
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
	return boot_up(copy.deepcopy(data))


def ft_part2(data):
	return 0


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

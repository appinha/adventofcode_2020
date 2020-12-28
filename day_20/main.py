# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core

# Import requirements
import re
import itertools as it
import numpy as np
from collections import defaultdict


input_file = sys.argv[1]


def ft_get_borders(tile):
	''' Get list of tile borders (as strings) in sequence N, E, S, W. '''
	border2str = lambda border: ''.join('0' if n == 0 else '1' for n in border)
	return [border2str(tile[0]), border2str(tile[:, -1]), \
			border2str(tile[-1]), border2str(tile[:, 0])]


def ft_input_parser(raw_input):
	'''
	Convert input into two dictionaries:
		- dc_tiles: ID number as key and tile grid (converted to a matrix of 1s
		and 0s so '#' are "countable") as value;
		- dc_borders: border (as string of 1s and 0s, including reversed) as key
		and list of ID numbers of tiles that contain such border as value.
	Also returns a list of corner tiles' ID numbers.
	'''
	dc_tiles = {}
	dc_borders = defaultdict(list)
	for block in raw_input:
		block = block.split('\n')
		id_nbr = int(re.findall(r'\d+', block[0])[0])
		dc_tiles[id_nbr] = np.array([[1 if c == '#' else 0 for c in line] \
										for line in block[1:]])
		for border in ft_get_borders(dc_tiles[id_nbr]):
			dc_borders[border].append(id_nbr)
			dc_borders[border[::-1]].append(id_nbr)
	ls_edges = [dc_borders[b][0] for b in dc_borders if len(dc_borders[b]) == 1]
	ls_corners = [id_n for id_n in set(ls_edges) if ls_edges.count(id_n) == 4]
	return dc_tiles, dc_borders, ls_corners


def ft_assemble_image(dc_tiles, dc_borders, ls_corners):
	''' Assemble full image by matching tile borders. '''
	NN = 0
	EE = 1
	SS = 2
	WW = 3

	def rotate(tile, ls_borders, border, inc):
		''' Rotate tile using given border index (orientation) in ls_borders for
		determining how many times it should be rotated 90 degrees. '''
		times = ls_borders.index(border) if border in ls_borders \
			else ls_borders.index(border[::-1])
		return np.rot90(tile, times + inc)

	def fill_in(ls_pos, dirct):
		''' Fill in tiles into grid (ls_pos) according to given direction. '''
		for y, x in ls_pos:
			prev_id = grid_ids[y - 1][x] if dirct == SS else grid_ids[y][x - 1]
			matching_border = ft_get_borders(dc_tiles[prev_id])[dirct]
			curr_id = (set(dc_borders[matching_border]) - {prev_id}).pop()
			curr_tile = dc_tiles[curr_id]
			curr_borders = ft_get_borders(curr_tile)
			grid_ids[y][x] = curr_id
			rot_tile = rotate(curr_tile, curr_borders, matching_border, \
								0 if dirct == SS else 1)
			opos_dir = NN if dirct == SS else WW
			if ft_get_borders(rot_tile)[opos_dir] != matching_border:
				rot_tile = np.fliplr(rot_tile) if dirct == SS \
						else np.flipud(rot_tile)
			dc_tiles[curr_id] = rot_tile

	# Setup empty (None) grid
	grid_side = int(np.sqrt(len(dc_tiles)))
	grid_ids = [[None] * grid_side for i in range(grid_side)]
	# Get first corner
	corner_1 = ls_corners[0]
	tile_1 = dc_tiles[corner_1]
	grid_ids[0][0] = corner_1
	# Correct its rotation so corner borders are oriented to N and W
	corner_borders = [i for i, border in enumerate(ft_get_borders(tile_1)) \
						if len(dc_borders[border]) == 1]
	if corner_borders != [NN, WW]:
		dc_tiles[corner_1] = np.rot90(tile_1, max(corner_borders))
	# Fill in first column of grid of ID numbers, going South
	fill_in(it.product(range(1, grid_side), [0]), SS)
	# Fill in rows starting from filled column (0, y), going East
	fill_in(it.product(range(grid_side), range(1, grid_side)), EE)
	return np.concatenate(\
			[np.concatenate(\
				[dc_tiles[id_n][1:-1, 1:-1] for id_n in grid_ids[y]], axis=1) \
			for y in range(grid_side)], axis=0)


def scan_sea(image):
	''' Scan sea for sea monsters, counting their occurrences, then subtract
	this to the total number of '#' in image (represented as 1s in matrix). '''
	sea_monster = [(0, 18), \
		(1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19), \
		(2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]
	img_side = image.shape[0]
	sm_side = lambda i: max(sea_monster, key = lambda v: v[i])[i]
	ls_pos = it.product(range(img_side - sm_side(0)), range(img_side - sm_side(1)))
	count_sea_monsters = sum(len(sea_monster) for y, x in ls_pos \
					if all(image[y + a][x + b] == 1 for a, b in sea_monster))
	return np.sum(image) - count_sea_monsters


def ft_part1(data):
	''' Calculate product of IDs of corner tiles. '''
	return np.prod(data[2])


def ft_part2(data):
	''' Assemble image, rotate and flip it in all 4 directions, then scan sea to
	determine how rough the waters are in the sea monsters' habitat. '''
	image = ft_assemble_image(*data)
	ls_rot_imgs = [np.rot90(image, r) for r in range(4)]
	ls_flp_imgs = [np.flipud(image) for image in ls_rot_imgs]
	return min([scan_sea(img) for img in it.chain(*[ls_rot_imgs + ls_flp_imgs])])


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2, delimiter='\n\n')

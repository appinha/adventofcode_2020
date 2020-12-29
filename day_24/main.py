# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core

# Import requirements
from collections import defaultdict


input_file = sys.argv[1]


# Hexagonal grid coordinates using complex numbers
dc_hex = {"ne": 1 + 1j, "e": 2, "se": 1 - 1j, \
			"sw": -1 - 1j, "w": -2, "nw": -1 + 1j}


def ft_input_parser(raw_input):
	'''Convert input into a dictionary of tiles, with tile's coordinate (pos) as
	key and its state - True for white and False for black - as value.'''
	dc_tiles = defaultdict(bool)
	for line in raw_input:
		pos = 0
		ls_dirs = line.replace('e', 'e ').replace('w', 'w ').split()
		for d in ls_dirs:
			pos += dc_hex[d]
		dc_tiles[pos] = not dc_tiles[pos]
	return dc_tiles


def ft_living_art_exhibit(dc_tiles, nbr_days):
	'''Simulate living art exhibit of lobby's tile floor for number of days.
	From given inital state of tile floor (dictionary of tiles) and number of
	days, return number of tiles that are black at the end of simulation.'''
	ls_rel = dc_hex.values()
	st_black = set(pos for pos in dc_tiles if dc_tiles[pos] == True)
	st_adjs = set(pos + rel for pos in st_black for rel in ls_rel)
	for _ in range(nbr_days):
		black2white = set(pos for pos in st_black \
				if sum(pos + rel in st_black for rel in ls_rel) not in [1, 2])
		white2black = set(pos for pos in st_adjs \
				if sum(pos + rel in st_black for rel in ls_rel) == 2)
		st_black = (st_black - black2white) | white2black
		st_new_adj = set(pos + rel for pos in white2black for rel in ls_rel)
		st_adjs = st_adjs | st_new_adj
	return len(st_black)


def ft_part1(data):
	'''Return number of tiles that are left with the black side up after parsing
	the input, i.e. at initial state of lobby's tile floor.'''
	return sum(data.values())


def ft_part2(data):
	'''Return number of tiles that will be black after 100 days of living art
	exhibit of lobby's tile floor.'''
	return ft_living_art_exhibit(data, 100)


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2)

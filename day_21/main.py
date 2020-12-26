# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
from collections import defaultdict


input_file = sys.argv[1]


def ft_match_ingr_algn(dc_algn):
	'''
	From dictionary of allergens (key) with list of possible ingredients that
	contain such allergen (value), find exact ingredient that contains allergen.
	'''
	for i in range(len(dc_algn)):
		for ch_al in dc_algn.keys():
			dc_algn = {al: dc_algn[al] - dc_algn[ch_al] \
				if len(dc_algn[ch_al]) == 1 and ch_al != al else dc_algn[al] \
				for al in dc_algn}
	return {key: dc_algn[key].pop() for key in sorted(dc_algn)}


def ft_input_parser(raw_input):
	'''
	Convert input into two dictionaries:
		- dc_ingr_count: ingredient as key and its occurrence count as value.
		- dc_algn: allergen as key and ingredient that contains such allergen
		as value.
	'''
	dc_ingr_count = defaultdict(int)
	dc_algn = defaultdict(set)
	for line in raw_input:
		ingrs, algns = line.split(" (contains ")
		st_ingrs = set(ingrs.split(' '))
		st_algns = set(algns[:-1].split(", "))
		for ingr in st_ingrs:
			dc_ingr_count[ingr] += 1
		for al in st_algns:
			dc_algn[al] = dc_algn[al] & st_ingrs if al in dc_algn else st_ingrs
	return dc_ingr_count, ft_match_ingr_algn(dc_algn)


def ft_part1(data):
	'''Find set of safe ingredients (ones that don't contain allergens) and
	count their occurrence in list of foods.'''
	dc_ingr_count, dc_algn = data
	st_safe_ingrs = dc_ingr_count.keys() - dc_algn.values()
	return sum(dc_ingr_count[ingr] for ingr in st_safe_ingrs)


def ft_part2(data):
	'''Get list of dangerous ingredients (already sorted by allergen).'''
	dc_algn = data[1]
	return ','.join(list(dc_algn.values()))


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

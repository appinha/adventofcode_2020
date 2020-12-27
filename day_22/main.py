# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core

# Import requirements
import copy


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	''''''
	return [[int(i) for i in block.split('\n')[1:]] for block in raw_input]


def ft_combat_game(d1, d2):
	'''Play combat game. Return winner's deck at end of game.'''
	while d1 and d2:
		wi_d, lo_d = [d1, d2] if d1[0] > d2[0] else [d2, d1]
		wi_d += [wi_d.pop(0), lo_d.pop(0)]
	return wi_d


def ft_rec_combat_game(d1, d2):
	'''Play recursive combat game. Return winner and its deck at end of game.'''
	st_seen_decks = set()
	while d1 and d2:
		if (tuple(d1), tuple(d2)) in st_seen_decks:
			return 1, d1
		st_seen_decks.add((tuple(d1), tuple(d2)))
		c1 = d1.pop(0)
		c2 = d2.pop(0)
		if len(d1) >= c1 and len(d2) >= c2:
			wi, _ = ft_rec_combat_game(d1[0:c1], d2[0:c2])
		else:
			wi = 1 if c1 > c2 else 2
		d1 += [c1, c2] if wi == 1 else []
		d2 += [c2, c1] if wi == 2 else []
	return wi, d1 if wi == 1 else d2


def ft_calc_score(deck):
	'''Calculate winning player's score.'''
	return sum((i + 1) * v for i, v in enumerate(reversed(d)))


def ft_part1(data):
	'''Play combat game. Return winning player's score'''
	return ft_calc_score(ft_combat_game(*copy.deepcopy(data)))


def ft_part2(data):
	'''Play recursive combat game. Return winning player's score'''
	return ft_calc_score(ft_rec_combat_game(*copy.deepcopy(data))[1])


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2, delimiter='\n\n')

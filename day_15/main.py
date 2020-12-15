# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
from collections import defaultdict


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	if input_file == "input_test.txt":
		return [line.split(',') for line in raw_input]
	else:
		return raw_input[0].split(',')


def play_elves_game(data, max_turn):
	dc_nbrs = defaultdict(list)
	turn = 1
	for nbr in data:
		dc_nbrs[int(nbr)].append(turn)
		turn += 1
	curr_nbr = int(nbr)
	while turn <= max_turn:
		if len(dc_nbrs[curr_nbr]) == 1:
			curr_nbr = 0
		else:
			curr_nbr = dc_nbrs[curr_nbr][-1] - dc_nbrs[curr_nbr][-2]
		dc_nbrs[curr_nbr].append(turn)
		turn += 1
	return curr_nbr


def run_parts(data, max_turn):
	if input_file == "input_test.txt":
		res = [play_elves_game(line, max_turn) for line in data]
	else:
		res = play_elves_game(data, max_turn)
	return res


def ft_part1(data):
	return run_parts(data, 2020)


def ft_part2(data):
	return run_parts(data, 30000000)


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

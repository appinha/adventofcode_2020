# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core


input_file = sys.argv[1]


class Node:
	'''Class for storing elements (cups) of linked list.'''
	def __init__(self, cup):
		self.cup = cup
		self.next = None

	def __repr__(self):
		return '[{} n({})]'.format(self.cup, self.next.cup)


def ft_input_parser(raw_input):
	'''Return list of cup labels (int) converted from input (string).'''
	return [int(n) for n in raw_input[0]]


def ft_get_dc_cups(ls_cups):
	'''Return dictionary of cups, with cup labels (from given list) as keys and
	corresponding Node objects (where Node.value = cup_label and Node.next
	points to next Node object as per list order) as values.'''
	dc_cups = {i: Node(i) for i in range(1, max(ls_cups) + 1)}
	for i, v in enumerate(ls_cups):
		dc_cups[v].next = dc_cups[ls_cups[(i + 1) % len(ls_cups)]]
	return dc_cups


def ft_play_cup_game(first, dc_cups, nbr_moves):
	'''Return updated dictionary of cups after playing crab's cup game.'''
	curr = dc_cups[first]
	for _ in range(nbr_moves):
		pick_up = [curr.next, curr.next.next, curr.next.next.next]
		curr.next = pick_up[-1].next
		dst = curr.cup - 1 if curr.cup > 1 else len(dc_cups)
		while dst in [curr.cup, pick_up[0].cup, pick_up[1].cup, pick_up[2].cup]:
			dst = dst - 1 if dst > 1 else len(dc_cups)
		pick_up[-1].next = dc_cups[dst].next
		dc_cups[dst].next = pick_up[0]
		curr = curr.next
	return dc_cups


def ft_part1(data):
	'''Return string with cup labels (only those after cup 1) upon simulating
	(playing) crab's cup game for 100 moves.'''
	dc_cups = ft_play_cup_game(data[0], ft_get_dc_cups(data), 100)
	res = ""
	p = dc_cups[1].next
	for _ in range(len(dc_cups) - 1):
		res += str(p.cup)
		p = p.next
	return res


def ft_part2(data):
	'''Return product of the two cup labels after cup 1 upon simulating
	(playing) crab's cup game for 10000000 moves.'''
	new_data = data + list(range(10, 1000001))
	dc_cups = ft_play_cup_game(data[0], ft_get_dc_cups(new_data), 10000000)
	return dc_cups[1].next.cup * dc_cups[1].next.next.cup


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2)

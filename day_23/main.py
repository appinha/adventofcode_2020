# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core

# Import requirements
import copy
from collections import deque


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	return [int(n) for n in raw_input[0]]


def ft_play_cup_game(ls_nbrs, nbr_moves):

	def find_dest(queue):
		n = queue.pop() - 1
		while n not in queue:
			n = n - 1 if n > 0 else max(queue)
		return n

	queue = deque(ls_nbrs)
	for _ in range(nbr_moves):
		curr = queue[0]
		queue.rotate(-1)
		pick_up = [queue.popleft() for _ in range(3)]
		dest = find_dest(copy.deepcopy(queue))
		queue.rotate(-(queue.index(dest) + 1))
		queue.extendleft(reversed(pick_up))
		queue.rotate(-(queue.index(curr) + 1))
	queue.rotate(-(queue.index(1)))
	queue.popleft()
	return ''.join(str(n) for n in queue)


def ft_part1(data):
	return ft_play_cup_game(data, 100)


# def ft_part2(data):
# 	return


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, False)

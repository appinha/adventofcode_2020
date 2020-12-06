from termcolor import colored


def get_input():
	'''
		Open input file and split string into list of lines.
	'''
	with open('input.txt', 'r') as f:
		input_string = f.read()
	return list(map(str, (input_string.split('\n'))))


def count_trees(lines, right, down):
	'''
		Count how many trees were encountered in map with given slope.
	'''
	count = 0
	x = 0
	for y in range(down, len(lines), down):
		x += right
		if x >= len(lines[y]):
			x = x - len(lines[y])
		if lines[y][x] == '#':
			count += 1
	return count


if __name__ == '__main__':

	part_one = colored("\nPart One:", 'magenta')
	part_two = colored("\nPart Two:", 'magenta')

	lines = get_input()

	## PART ONE
	p1_res = count_trees(lines, 3, 1)

	## PART TWO
	inputs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
	p2_res = []
	for i in inputs:
		p2_res.append(count_trees(lines, i[0], i[1]))
	p2_res_prod = 1
	for r in p2_res:
		p2_res_prod *= r

	print(part_one, p1_res)
	print(part_two, p2_res_prod)
	print()
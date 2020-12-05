from termcolor import colored

# Open input file and split string into list of lines
with open('input.txt', 'r') as f:
	input_string = f.read()
lines = list(map(str, (input_string.split('\n'))))

def count_trees(right, down):
	count = 0
	x = 0
	for y in range(down, len(lines), down):
		x += right
		if x >= len(lines[y]):
			x = x - len(lines[y])
		if lines[y][x] == '#':
			count += 1
	return count

## PART ONE
print(colored("\n--- Part One ---", 'magenta'))
print(count_trees(3, 1))

## PART TWO
print(colored("\n--- Part Two ---", 'magenta'))
res_1 = count_trees(1, 1)
res_2 = count_trees(3, 1)
res_3 = count_trees(5, 1)
res_4 = count_trees(7, 1)
res_5 = count_trees(1, 2)
print(res_1, "*", res_2, "*", res_3, "*", res_4, "*", res_5, "=", \
		res_1 * res_2 * res_3 * res_4 * res_5)

print()
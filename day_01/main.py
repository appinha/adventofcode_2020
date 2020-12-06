from termcolor import colored


def get_input():
	'''
		Open input file and split string into list of numbers.
	'''
	with open('input.txt', 'r') as f:
		input_string = f.read()
	return list(map(int, (input_string.split('\n'))))


if __name__ == '__main__':

	part_one = colored("\nPart One:", 'magenta')
	part_two = colored("\nPart Two:", 'magenta')

	nbrs = get_input()

	# Loop through list of numbers n times for combinatorial analysis
	for i in range(len(nbrs)):
		for j in range(i + 1, len(nbrs)):
			# PART ONE - Check if sum of two numbers is equal to 2020
			if (nbrs[i] + nbrs[j] == 2020):
				# PART ONE - Get numbers
				p1_nbr_1 = nbrs[i]
				p1_nbr_2 = nbrs[j]
			for k in range(j + 1, len(nbrs)):
				# PART TWO - Check if sum of three numbers is equal to 2020
				if (nbrs[i] + nbrs[j] + nbrs[k] == 2020):
					# PART TWO - Get numbers
					p2_nbr_1 = nbrs[i]
					p2_nbr_2 = nbrs[j]
					p2_nbr_3 = nbrs[k]

	# Print numbers and its products
	print(part_one, p1_nbr_1, "*", p1_nbr_2, "=", p1_nbr_1 * p1_nbr_2)
	print(part_two, p2_nbr_1, "*", p2_nbr_2, "*", p2_nbr_3, "=", \
			p1_nbr_1 * p1_nbr_2 * p2_nbr_3)
	print()

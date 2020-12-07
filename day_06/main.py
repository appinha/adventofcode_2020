from termcolor import colored


def get_input():
	'''
		Open input file and split string into list of groups.
	'''
	with open('input.txt', 'r') as f:
		input_string = f.read()
	return list(map(str, (input_string.split('\n\n'))))


def get_ls_uniques(group):
	'''
		Get list of unique values (characters).
	'''
	group_flat = group.replace('\n', '')
	return list(set(group_flat))


def p1_count(group):
	'''
		Count how many unique values in group answers.
	'''
	return len(get_ls_uniques(group))


def p2_count(group):
	'''
		Count how many answers are present in all group members answers.
	'''
	nbr_members = group.count('\n') + 1
	ls_uniques = get_ls_uniques(group)
	count = 0
	for c in ls_uniques:
		if group.count(c) == nbr_members:
			count += 1
	return count


if __name__ == '__main__':

	part_one = colored("\nPart One:", 'magenta')
	part_two = colored("\nPart Two:", 'magenta')

	ls_groups = get_input()

	p1_count_sum = 0
	p2_count_sum = 0
	for group in ls_groups:
		p1_count_sum += p1_count(group)
		p2_count_sum += p2_count(group)

	print(part_one, p1_count_sum)
	print(part_two, p2_count_sum)
	print()

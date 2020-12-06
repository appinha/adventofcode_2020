from termcolor import colored
import re


def get_input():
	'''
		Open input file and split string into list of lines.
	'''
	with open('input.txt', 'r') as f:
		input_string = f.read()
	return list(map(str, (input_string.split('\n'))))


def split_line_values(lines):
	'''
		Split with regex each line's values - two integers, a character and a
		string - into sublists.
	'''
	pwds = []
	for i in range(len(lines)):
		pwds.append(re.split('-| |: ', lines[i]))
	return pwds


# Values' indexes
IND_1 = 0
IND_2 = 1
CHAR = 2
STR = 3


def p1_check(pwd, ind_1, ind_2):
	'''
		Check if given password is valid according to Part One password policy.
	'''
	count = pwd[STR].count(pwd[CHAR])
	if ind_1 <= count <= ind_2:
		return True
	return False


def p2_check(line, ind_1, ind_2):
	'''
		Check if given password is valid according to Part Two password policy.
	'''

	def check(line, ind):
		if ind < len(line[STR]):
			if line[CHAR] == line[STR][ind]:
				return 1
		return 0

	count = check(line, ind_1) + check(line, ind_2)
	if count == 1:
		return True
	return False


if __name__ == '__main__':

	part_one = colored("\nPart One:", 'magenta')
	part_two = colored("\nPart Two:", 'magenta')

	pwds = split_line_values(get_input())

	valid_pwds_1 = []
	valid_pwds_2 = []
	for i in range(len(pwds)):
		if p1_check(pwds[i], int(pwds[i][IND_1]), int(pwds[i][IND_2])):
			valid_pwds_1.append(pwds[i])
		if p2_check(pwds[i], int(pwds[i][IND_1]) - 1, int(pwds[i][IND_2]) - 1):
			valid_pwds_2.append(pwds[i])

	print(part_one, colored("Valid passwords =", 'blue'), len(valid_pwds_1))
	print(part_two, colored("Valid passwords =", 'blue'), len(valid_pwds_2))
	print()
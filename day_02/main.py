from termcolor import colored
from parse_input import pwds


IND_1 = 0
IND_2 = 1
CHAR = 2
STR = 3


## PART ONE
print(colored("\n--- Part One ---", 'magenta'))

def part_one(pwd, ind_1, ind_2):
	count = pwd[STR].count(pwd[CHAR])
	if ind_1 <= count <= ind_2:
		return True
	return False

valid_pwds_1 = []
for i in range(len(pwds)):
	if part_one(pwds[i], int(pwds[i][IND_1]), int(pwds[i][IND_2])):
		valid_pwds_1.append(pwds[i])

print(colored("Valid passwords:", 'blue'), len(valid_pwds_1))


## PART TWO
print(colored("\n--- Part Two ---", 'magenta'))

def part_two_check(line, ind):
	if ind < len(line[STR]):
		if line[CHAR] == line[STR][ind]:
			return 1
	return 0

def part_two(line, ind_1, ind_2):
	count = part_two_check(line, ind_1)
	count += part_two_check(line, ind_2)
	if count == 1:
		return True
	return False

valid_pwds_2 = []
for i in range(len(pwds)):
	if part_two(pwds[i], int(pwds[i][IND_1]) - 1, int(pwds[i][IND_2]) - 1):
		valid_pwds_2.append(pwds[i])

print(colored("Valid passwords:", 'blue'), len(valid_pwds_2))

print()
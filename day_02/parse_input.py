import re


# Open input file and split string into list of lines
with open('input.txt', 'r') as f:
	input_string = f.read()
lines = list(map(str, (input_string.split('\n'))))

# Split with regex each line values into sublists
pwds = []
for i in range(len(lines)):
	pwds.append(re.split('-| |: ', lines[i]))


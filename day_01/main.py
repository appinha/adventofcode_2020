from termcolor import colored

with open('input.txt', 'r') as f:
	input_string = f.read()

nbrs = list(map(int, (input_string.split('\n'))))

for i in range(len(nbrs)):
	for j in range(i + 1, len(nbrs)):
		if (nbrs[i] + nbrs[j] == 2020):
			print(nbrs[i], "*", nbrs[j], "=", nbrs[i] * nbrs[j])
		for k in range(j + 1, len(nbrs)):
			if (nbrs[i] + nbrs[j] + nbrs[k] == 2020):
				print(nbrs[i], "*", nbrs[j], "*", nbrs[k], "=", \
						nbrs[i] * nbrs[j] * nbrs[k])

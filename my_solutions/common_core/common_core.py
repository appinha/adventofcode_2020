from termcolor import colored
import time


def ft_core(input_file, ft_input_parser, ft_part1=False, ft_part2=False, \
			delimiter='\n'):
	'''Common framework for solving AoC puzzels.'''
	start_time = time.time()

	with open(input_file, 'r') as f:
		raw_input = list(map(str, (f.read().split(delimiter))))

	data = ft_input_parser(raw_input)

	print()
	if ft_part1:
		print(colored("Part One:", 'magenta'), ft_part1(data))
	if ft_part2:
		print(colored("Part Two:", 'magenta'), ft_part2(data))

	print(colored("\nTime:", 'blue'), time.time() - start_time, "\n")

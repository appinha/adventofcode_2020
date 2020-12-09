# Import common core
import sys
sys.path.append('../common_core')
from common_core import core


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	''' Convert given input to dictionary of enumerated instructions '''
	def parse_line(line):
		instruction, value = line.split(' ')
		return [[instruction, int(value)], 0]

	return dict(list(enumerate([parse_line(line) for line in raw_input])))


def interpreter(tp_instr):
	''' Interpret given instruction and return index and acc increments. '''
	if tp_instr[0] == 'acc':
		return 1, tp_instr[1]
	if tp_instr[0] == 'jmp':
		return tp_instr[1], 0
	if tp_instr[0] == 'nop':
		return 1, 0


INSTR = 0
COUNT = 1

def run_instr(data):
	''' Run instructions from data and return resulting acc value. '''
	def reset_count(data):
		for i in data:
			data[i][COUNT] = 0

	i = 0
	acc = 0
	while data[i][COUNT] == 0:
		data[i][COUNT] += 1
		res_i, res_acc = interpreter(data[i][INSTR])
		i += res_i
		acc += res_acc
		if i >= len(data):
			reset_count(data)
			return [acc, True]
	reset_count(data)
	return [acc, False]


def ft_part1(data):
	return run_instr(data)[0]


def ft_part2(data):
	''' Loop through instructions, changing one per time and testing if program
		terminates. '''
	def change_instr(st_instr):
		''' Change given instruction and test if program terminates. '''
		if st_instr == 'nop':
			data[i][INSTR][0] = 'jmp'
		elif st_instr == 'jmp':
			data[i][INSTR][0] = 'nop'
		res = run_instr(data)
		if res[1] == True:
			data[i][INSTR][0] = st_instr
			return res
		else:
			data[i][INSTR][0] = st_instr
			return False

	for i in data:
		if data[i][INSTR][0] == 'acc' or \
			(data[i][INSTR][0] == 'nop' and data[i][INSTR][1] == 0):
			continue
		res = change_instr(data[i][INSTR][0])
		if res:
			break

	return res[0]


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2)

from termcolor import colored


def get_input():
	'''
		Open input file and split string into list of boarding passes.
	'''
	with open('input.txt', 'r') as f:
		input_string = f.read()
	return list(map(str, (input_string.split('\n'))))


def bpcode2seatID(bpcode):
	'''
		Convert boarding pass code to seat ID.
	'''

	def b2i(code, char):
		'''
			Convert binary pattern to integer.
		'''
		loc = 0
		exp = len(code) - 1
		for c in code:
			if c == char:
				loc += 2 ** exp
			exp -= 1
		return loc

	row = b2i(bpcode[0:7], 'B')
	col = b2i(bpcode[7:], 'R')

	return row * 8 + col


if __name__ == '__main__':

	part_one = colored("\nPart One:", 'magenta')
	part_two = colored("\nPart Two:", 'magenta')

	lines = get_input()

	ls_seat_ID = []
	for bpcode in lines:
		ls_seat_ID.append(bpcode2seatID(bpcode))

	seatID_range = [*range(min(ls_seat_ID), max(ls_seat_ID) + 1)]
	for n in seatID_range:
		if n not in ls_seat_ID:
			my_seat = n
			break

	print(part_one, max(ls_seat_ID))
	print(part_two, my_seat)
	print()

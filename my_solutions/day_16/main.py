# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core

# Import requirements
import re
from itertools import chain
from numpy import prod


input_file = sys.argv[1]


class Field:
	''' Class for storing information on each ticket field. '''
	def __init__(self, name, arange, ls_tickets):
		self.name = name
		self.ls_indexes, self.qty_True = self.parse(arange, ls_tickets)

	def __str__(self):
		return ("\nField: {}, Qty Trues: {}, Indexes: {}\n"\
				).format(self.name, self.qty_True, self.ls_indexes)

	def __repr__(self):
		return self.__str__()

	def parse(self, arange, ls_tickets):
		''' Parse list of tickets to get all possible indexes for field. '''
		res = []
		for col in range(len(ls_tickets[0])):
			for row in range(len(ls_tickets)):
				if ls_tickets[row][col] not in arange:
					break
				if row == (len(ls_tickets) - 1):
					res.append(col)
		return res, len(res)

	def get_index(self, ls_found_i):
		''' From given list of found indexes (for other fields), remove such
			indexes from field's list of possible indexes. Return the remaining
			index (i.e. the correct index for the field). '''
		ls_found_i = sorted(ls_found_i)
		for found_i in ls_found_i:
			self.ls_indexes.remove(found_i)
		return self.ls_indexes[0]


def ft_input_parser(raw_input):
	''' Convert input to dictionary with parsed text blocks into keys. '''
	def get_fields(ls_lines):
		''' Convert 1st text block into dictionary with ticket fields as keys
			and range values as a list of all numbers in given ranges. '''
		def get_ranges(line):
			nbrs = list(map(int, re.findall(r'[\d]+', line)))
			ranges = [list(range(nbrs[i], nbrs[i + 1] + 1)) \
						for i in range(0, len(nbrs), 2)]
			return sum(ranges, [])
		return {line.split(':')[0]: get_ranges(line) for line in ls_lines}

	def get_my_ticket(ls_lines):
		''' Convert 2nd text block into a list with my ticket information. '''
		return list(map(int, ls_lines[1].split(',')))

	def get_tickets(ls_lines, ):
		''' Convert 3rd text block into a list of lists with nearby tickets. '''
		return [list(map(int, line.split(','))) for line in ls_lines[1:]]

	return {'fields': get_fields(raw_input[0].split('\n')), \
			'my_ticket': get_my_ticket(raw_input[1].split('\n')), \
			'tickets': get_tickets(raw_input[2].split('\n'))}


def get_all_ranges(data):
	''' Get a list with numbers in all fields' ranges. '''
	return list(set(chain.from_iterable(data['fields'].values())))


def get_valid_tickets(data, all_ranges):
	''' Get all valid tickets (according to fields' ranges). '''
	def check_ticket(ticket, all_ranges):
		for nbr in ticket:
			if nbr not in all_ranges:
				return False
		return True
	return [t for t in data['tickets'] if check_ticket(t, all_ranges)]


def ft_part1(data):
	''' Sum all invalid numbers (according to fields' ranges) in tickets. '''
	all_ranges = get_all_ranges(data)
	all_ticket_nbrs = list(chain.from_iterable(data['tickets']))
	return sum(n for n in all_ticket_nbrs if n not in all_ranges)


def ft_part2(data):
	''' Get only valid tickets and parse them to find in which order the fields
		appear in tickets. Return the product of values in my ticket of fields
		that contain the word "departure". '''
	def find_fields_indexes(ls_fields):
		''' Loop through list of Field-class objects to find their indexes (i.e.
			order of appearance in tickets). '''
		dc_fields_i = {}
		ls_found_i = []
		i = 1
		while ls_fields:
			for f in ls_fields:
				if f.qty_True == i:
					index = f.get_index(ls_found_i)
					dc_fields_i[index] = f.name
					ls_found_i.append(index)
					ls_fields.remove(f)
					break
			i += 1
		return dc_fields_i

	val_tickets = get_valid_tickets(data, get_all_ranges(data))
	ls_fields = [Field(k, v, val_tickets) for k, v in data['fields'].items()]
	dc_fields_i = find_fields_indexes(ls_fields)
	dc_my_ticket = {dc_fields_i[i]: v for i, v in enumerate(data['my_ticket'])}
	return prod([v for k, v in dc_my_ticket.items() if k.find('departure') >= 0])


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, ft_part2, delimiter='\n\n')

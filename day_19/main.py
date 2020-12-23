# Import common core
import sys
sys.path.append('../common_core')
from common_core import core


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	''' Convert input to dictionary with parsed text blocks into keys. '''
	def get_rules(ls_lines):
		''' Convert 1st text block into dictionary with rule number as key and
		rule specifications as a list of lists of other rule numbers. '''
		def parse_line(line):
			''' Convert line (string) into key and value for dictionary. '''
			key, value = line.split(': ')
			if value in ['"a"', '"b"']:
				return key, value[1]
			return key, [v.split(' ') for v in value.split(' | ')]

		return dict([parse_line(line) for line in ls_lines])

	def get_messages(ls_lines):
		''' Convert 2nd text block into a list of messages (strings). '''
		return [line for line in ls_lines]

	return {'rules': get_rules(raw_input[0].split('\n')), \
			'msgs': get_messages(raw_input[1].split('\n'))}


def ft_check_msg(dc_rules, msg, ls_rules):
	''' Check if message match rules, returns True if so. '''
	# If no rules are left for checking (in 'ls_rules') and no characters
	# remain in 'msg' (len(msg) == 0), it means message was completely checked
	# and is valid (returns True); else, message is invalid (returns False).
	if not ls_rules:
		return len(msg) == 0
	# Get specifications for first rule in 'ls_rules' and remove it from list.
	ls_specs = dc_rules[ls_rules.pop(0)]
	# If such specifications is one of valid characters and 'msg' starts with
	# it, return a call to function (recursive) with remaining characters
	# (msg[1:]); else, continue checking if any of the remaining rules (with
	# specifications added to the list of rules) match.
	if ls_specs in ['a', 'b']:
		if msg.startswith(ls_specs):
			return ft_check_msg(dc_rules, msg[1:], ls_rules)
	else:
		return any(ft_check_msg(dc_rules, msg, s + ls_rules) for s in ls_specs)


def ft_part1(data):
	''' Count how many messages completely match rule 0 (i.e. returned True).'''
	return sum(ft_check_msg(data['rules'], msg, ['0']) for msg in data['msgs'])


def ft_part2(data):
	''' Count how many messages completely match rule 0 (i.e. returned True)
	with updated rules.'''
	data['rules']['8'] = [['42'], ['42', '8']]
	data['rules']['11'] = [['42', '31'], ['42', '11', '31']]
	return sum(ft_check_msg(data['rules'], msg, ['0']) for msg in data['msgs'])


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2, delimiter='\n\n')

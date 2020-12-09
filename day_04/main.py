# Import common core
import sys
sys.path.append('../common_core')
from common_core import core

# Import requirements
import re
import json


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	''' Convert passport string to dict. '''

	def parse_line(line):
		line = line.replace('\n', ' ')
		line = re.sub(r'([a-z]+):([a-z\d#]+)', r'"\1":"\2",', line)
		return json.loads('{' + line[:-1] + '}')

	return [parse_line(line) for line in raw_input]


def validate_passports(data):

	def check(dc_item):
		if ('cid' in dc_item and len(dc_item) == 8) or \
			('cid' not in dc_item and len(dc_item) == 7):
			return True
		return False

	return [dc_item for dc_item in data if check(dc_item)]


def check_year(string, field):
	''' Check if year value is valid. '''
	if len(string) == 4:
		if (field == 'byr' and 1920 <= int(string) <= 2002) or \
			(field == 'iyr' and 2010 <= int(string) <= 2020) or \
			(field == 'eyr' and 2020 <= int(string) <= 2030):
			return True
	return False


def check_height(string):
	''' Check if height value is valid. '''
	nbr = int(re.findall(r'\d+', string)[0])
	if (string[-2:] == 'cm' and 150 <= nbr <= 193) or \
		(string[-2:] == 'in' and 59 <= nbr <= 76):
		return True
	return False


def check_hair_colour(string):
	''' Check if hair colour value is valid. '''
	if string[0] == '#' and len(string) == 7:
		try:
			int(string[1:7], 16)
			return True
		except ValueError:
			return False
	return False


def check_eye_colour(string):
	''' Check if eye colour value is valid. '''
	colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	if string in colours:
		return True
	return False


def check_pid(string):
	''' Check if PID value is valid. '''
	if len(string) == 9:
		try:
			int(string)
			return True
		except ValueError:
			return False
	return False


def validate_fields(dc_passport):
	''' Validate passport's field values. '''

	def check_years(dc_passport):
		for field in ['byr', 'iyr', 'eyr']:
			if check_year(dc_passport.get(field), field) == False:
				return False
		return True

	def check_fields(dc_passport):
		dc_fields = {'hgt': check_height, \
					'hcl': check_hair_colour, \
					'ecl': check_eye_colour, \
					'pid': check_pid}
		for key in dc_fields:
			if dc_fields[key](dc_passport.get(key)) == False:
				return False
		return True

	if check_years(dc_passport) == False or \
		check_fields(dc_passport) == False:
		return False
	return True


def ft_part1(data):
	return len(validate_passports(data))


def ft_part2(data):
	ls_valid_passports = validate_passports(data)
	return len([dc_item for dc_item in ls_valid_passports if validate_fields(dc_item)])


if __name__ == '__main__':
	core(input_file, ft_input_parser, ft_part1, ft_part2, delimiter="\n\n")

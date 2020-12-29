# Import common core
import sys
sys.path.append('../common_core')
from common_core import ft_core


input_file = sys.argv[1]


def ft_input_parser(raw_input):
	'''Convert input into list of public keys (integers).'''
	return [int(line) for line in raw_input]


def ft_get_encryption_key(public_key_1, public_key_2):
	'''Calculate encryption key of given public key pair.'''
	def get_loop_size(public_key):
		'''Find loop size of given public key.'''
		nbr = 1
		loop_size = 0
		while nbr != public_key:
			nbr = (nbr * 7) % 20201227
			loop_size += 1
		return loop_size

	return pow(public_key_1, get_loop_size(public_key_2), 20201227)


def ft_part1(data):
	'''Get encryption key of handshake.'''
	return ft_get_encryption_key(*data)


if __name__ == '__main__':
	ft_core(input_file, ft_input_parser, ft_part1, False)

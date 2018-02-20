
import eqs_tidal


class LoveNumberCalc(object):
	
	stellar_data = []
	
	def __init__(self, stellar_data):
		self.stellar_data = stellar_data
		print ('__init__')


	def print_love_numbers(self):
		for el in self.stellar_data:
			k_2 = eqs_tidal.k_2_politrope(el[0],el[1])
			print ('n: %2.2f, M/G = %2.5e, k_2 (tab) = %2.5f, k_2 (calc) = %2.5f' % (el[0],el[1], el[2],k_2))
	

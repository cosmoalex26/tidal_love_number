#!/usr/bin/python

import tidal_calc

import csv


def main():
	
	stellar_data = []


	with open('../data/hinderer.csv', 'r') as csvfile:
		#ratio_reader = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
		ratio_reader = csv.DictReader(csvfile, delimiter=',')
		#for row in ratio_reader:
		for line in ratio_reader:
			stellar_data.append([
				float(line['n'].strip()),
				float(line['M_R'].strip()), 
				float(line['k2'].strip())])

	loveNumberCalc = tidal_calc.LoveNumberCalc(stellar_data)
	
	loveNumberCalc.print_love_numbers()
	
	
	
  
if __name__== "__main__":
	main()

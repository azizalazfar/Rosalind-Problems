from collections import Counter

mass_table = {
	"A" : 71.03711,
	"C" : 103.00919,
	"D" : 115.02694,
	"E" : 129.04259,
	"F" : 147.06841,
	"G" : 57.02146,
	"H" : 137.05891,
	"I" : 113.08406,
	"K" : 128.09496,
	"L" : 113.08406,
	"M" : 131.04049,
	"N" : 114.04293,
	"P" : 97.05276,
	"Q" : 128.05858,
	"R" : 156.10111,
	"S" : 87.03203,
	"T" : 101.04768,
	"V" : 99.06841,
	"W" : 186.07931,
	"Y" : 163.06333,
}

# with open('1.txt') as file:
# 	protein = file.read().strip('\n').strip(' ')
protein = input("Enter protein seq here: ")

def mass_calc(protein):
	mass = 0
	AAs = Counter(protein)
	for aa, count in AAs.items():
		mass += [value*count for key,value in mass_table.items() if key == aa][0]
	return mass
print("\n")
print("Mass of input sequence: ",mass_calc(protein))
input("""

Press ENTER to close the window......""")

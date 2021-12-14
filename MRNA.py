from functools import reduce
from operator import mul
freq_table = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2,
    'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    'STOP': 3
    }

with open('rosalind_mrna.txt') as file:
	pr_seq = file.read()
to_multiply = []
for i in range(len(pr_seq)):
	aa = pr_seq[i]
	for key,value in freq_table.items():
		if key == aa:
			to_multiply.append(value)
	
to_multiply.append(3)

print(reduce(mul, to_multiply)%1000000)
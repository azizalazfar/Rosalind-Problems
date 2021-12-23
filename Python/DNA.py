with open('rosalind_rna.txt') as f:
	dataset = f.read()

print(dataset.count('A'), dataset.count('C'), dataset.count('G'), dataset.count('T'), sep = ' ') 

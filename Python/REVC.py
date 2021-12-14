with open("rosalind_revc.txt") as f:
	sequence = f.read()


def ComplementDNA(seq):
	complement = []
	reverse_DNA = seq[ :: -1]
	for base in reverse_DNA:
		if base == "A":
			complement.append("T")
		elif base == "G":
			complement.append("C")
		elif base == "C":
			complement.append("G")
		elif base == "T":
			complement.append("A")
	return print(''.join(complement))

ComplementDNA(sequence)
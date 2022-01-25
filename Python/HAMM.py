def Hammdist(txt1, txt2):
	return len([x for x,y in zip(txt1, txt2) if x != y])

with open('rosalind_hamm.txt') as f:
	seq_1, seq_2 = f.read().splitlines()

print(Hammdist(seq_1, seq_2))

with open('rosalind_rna.txt') as f:
	dataset = f.read()

def transcription(sequence):
	RNA = []
	for i in range(len(sequence)):
		if sequence[i] == 'A':
			RNA.append('A')
		elif  sequence[i] == 'C':
			RNA.append('C')
		elif  sequence[i] == 'G':
			RNA.append('G')
		elif  sequence[i] == 'T':
			RNA.append('U')
	print(*RNA, sep='')

#transcription(dataset)

#print(dataset.replace('T', 'U'))

print(input('Enter sequence here: ').replace('T','U'))


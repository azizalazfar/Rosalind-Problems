with open('rosalind_subs.txt') as file:
	data = file.read().split('\n')

DNA,motif = data[0],data[1]
positions = []
for i in range(len(DNA)-len(motif)):
	if DNA[i:i+len(motif)] == motif:
		positions.append(str(i+1))

print(' '.join(positions))
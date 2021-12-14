import numpy as np
from collections import Counter,defaultdict
import regex
from Bio import SeqIO



# with open('test.txt') as fasta:
# 	data = fasta.read()
# 	print(data)
# 	relist = regex.split('>Rosalind_', regex.sub('\n','', data))[1:]
# 	tidy_data = []
# 	for elem in relist:
# 		tidy_data.append(''.join(list(elem)[4:]))
tidy_data = []
with open('rosalind_cons.txt') as file:
	for org in SeqIO.parse(file, 'fasta'):
		tidy_data.append(str(org.seq))

transposed_matrix = np.matrix([list(elem) for elem in tidy_data]).T.tolist()

transposed_list = []
for sublist in transposed_matrix:
	transposed_list.append(''.join(sublist))


profile = {'A':[], 'C': [], 'G':[], 'T':[]}

for i in range(len(transposed_list)):
	count = {'A':transposed_list[i].count('A'),'C': transposed_list[i].count('C'),'G':transposed_list[i].count('G'),'T':transposed_list[i].count('T')}
	for key1, val1 in profile.items():
		for key2, val2 in count.items():
			if key1 == key2:
				val1.extend(str(val2))
profile_as_list = []
	

retransposed_matrix = np.matrix([list(value) for key, value in profile.items()]).T.tolist()
consensus = []
for sublist in retransposed_matrix:
	#for i in range(len(sublist)):
	
	if sublist.index(max(sublist)) == 0:
		consensus.append('A')
	elif sublist.index(max(sublist)) == 1:
		consensus.append('C')
	elif sublist.index(max(sublist)) == 2:
		consensus.append('G')
	elif sublist.index(max(sublist)) == 3:
		consensus.append('T')


print(''.join(consensus))
for key,values in profile.items():
	print(key+': '+' '.join(values))



	

from Bio import SeqIO

def GC(text):
	count = 0
	for i in range(len(text)):
		if text[i] == 'G' or text[i] == 'C':
			count += 1
	return count/len(text)*100

with open('rosalind_gc.txt', 'r') as data:
	max_GC, max_ID = 0,''
	for record in SeqIO.parse(data, 'fasta'):
		seq, ID = record.seq, record.ID
		gc = round(GC(seq), 6)
		print('GC content of '+ ID + ' : ' + str(gc) + '%')
		if gc > max_GC:
			max_GC = gc
			max_ID = ID
	print()		
		



#print(GC(''))

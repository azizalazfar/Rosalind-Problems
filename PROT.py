import argparse
import os.path
import sys
import pandas as pd

def RNA2AA(seq):
	AA_seq = list()
	for i in range(0,len(seq),3):
		if seq[i:i+3] in codon_list:
			if AA_Letter[codon_list.index(str(seq[i:i+3]))] == 'Stop':
				break
			else:
				AA_seq.append(AA_Letter[codon_list.index(str(seq[i:i+3]))])

	print(''.join(AA_seq))


# with open('rosalind_prot.txt') as file:
# 	DNAseq = file.read()
# 	RNA2AA(DNAseq)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Translating RNA into Protein')
	parser.add_argument('-inf','--infile', type = argparse.FileType('r'), metavar='FILE', default = sys.stdin, required = True, help='Please input file path')
	args = parser.parse_args()
	print(args.infile)
	#indir = os.path.join(os.getcwd(), args.filepath)
	with open(os.getcwd(args.infile)) as data:
		raw = data.read().splitlines()
		if raw[0].startswith('>'):
			RNAseq = raw[1:]
		else:
			RNAseq = raw
		

	codon_df = pd.read_csv('codon.txt', sep="\t", header = 0)
	codon_list, AA_Letter = list(codon_df['codon']), list(codon_df['letter'])


	RNA2AA(RNAseq)

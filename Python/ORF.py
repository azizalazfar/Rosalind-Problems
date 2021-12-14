import regex as re

codon_table = {
'TTT' : 'F', 'CTT' : 'L', 'ATT' : 'I', 'GTT' : 'V', 'TTC' : 'F', 'CTC' : 'L', 'ATC' : 'I', 'GTC' : 'V',
'TTA' : 'L', 'CTA' : 'L', 'ATA' : 'I', 'GTA' : 'V', 'TTG' : 'L', 'CTG' : 'L', 'ATG' : 'M', 'GTG' : 'V',
'TCT' : 'S', 'CCT' : 'P', 'ACT' : 'T', 'GCT' : 'A', 'TCC' : 'S', 'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A',
'TCA' : 'S', 'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A', 'TCG' : 'S', 'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A',
'TAT' : 'Y', 'CAT' : 'H', 'AAT' : 'N', 'GAT' : 'D', 'TAC' : 'Y', 'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D',
'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E', 'CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E', 'TGT' : 'C', 'CGT' : 'R',
'AGT' : 'S', 'GGT' : 'G', 'TGC' : 'C', 'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G', 'CGA' : 'R', 'AGA' : 'R',
'GGA' : 'G', 'TGG' : 'W', 'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G',
}

stop_signs = ['TAA', 'TAG', 'TGA']



def RevComp(seq):
	'''
	param: seq = a DNA string
	'''
	return seq.translate(str.maketrans("ACGT", "TGCA"))[::-1]

def Translator(codonlist):
	'''
	param: codonlist = a list of codons staring with 'ATG' and ending with any of 'TAA', 'TAG' or 'TGA'
	'''
	peptide = ""
	for codon in codonlist:
		if codon in stop_signs:
			return peptide
		else:
			peptide += codon_table[codon]
	return peptide


def ORF(DNA):
	'''
	param DNA = a string 
	'''
	peptides = [] 
	ORframes = [DNA, DNA[1:],DNA[2:]]     # 3 open reading frames
        
	for frame in ORframes:
		for i in range(0,len(frame),3):                # iterating over reading frame in steps of 3
			if frame[i:i+3] == 'ATG':                  # checking for start codon
				codons = list(filter(lambda elem : len(elem) == 3 ,re.findall('...?',frame[i:])))    # all codons from 'ATG'-> end of frame then filter for short seqments
				if len(set(codons).intersection(set(stop_signs))) > 0:   # checking for presence of stop codons(so there is no segments without stop codons)
					peptides.append(Translator(codons)) # translate the segment and append it to main list
	return peptides


with open('rosalind_orf.txt') as file:
	lines = file.read().split('\n')
	seq = ''
	for line in lines:
		if line.startswith('>') or len(line) == 0:
			pass
		else:
			seq += line

print('\n'.join(set(ORF(seq) + ORF(RevComp(seq)))))

with open('main_out.txt', 'w') as file:
	file.write('\n'.join(set(ORF(seq) + ORF(RevComp(seq)))))

import re

from Bio.SeqIO.FastaIO import SimpleFastaParser


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
	peptide = []
	for i in range(len(DNA)):
		if DNA[i:i+3] == 'ATG':
			codons = list(filter(lambda elem: len(elem) == 3, re.findall('...?', DNA[i:])))
			if len(set(codons).intersection(set(stop_signs))) > 0:
				peptide.append(Translator(codons))
	
	return max(peptide, key = len)

def Splicer(dna, intronlist):
	spliced_form = dna
	for intron in intronlist:
		spliced_form = re.sub(intron, '', spliced_form)
	return spliced_form

with open('rosalind_splc.txt') as handle:
	seq = []
	for element in SimpleFastaParser(handle):
		seq.append(element[1])

DNA, introns = seq[0], sorted(seq[1:],key = len)
sequence = Splicer(DNA,introns)

with open('output_slpc.txt', 'w') as file:
	file.write(ORF(sequence))

print(ORF(sequence))
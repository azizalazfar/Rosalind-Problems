from Bio.SeqIO.FastaIO import SimpleFastaParser
from collections import OrderedDict

with open('rosalind_grph.txt') as handle:
    data = OrderedDict(SimpleFastaParser(handle))


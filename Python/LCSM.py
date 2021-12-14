from os import remove


with open('rosalind_lcsm.txt') as handle:
    sequences = handle.read().splitlines()
    for line in sequences:
        if line.startswith('>'):
            sequences.remove(line)


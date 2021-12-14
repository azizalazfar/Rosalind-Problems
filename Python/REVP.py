

with open("rosalind_revp.txt") as file:
    lines = file.read().strip(' ').split("\n")
    sequences = []
    for line in lines:
        if line.startswith(">"):
            pass
        else:
            sequences.append(line)
sequences = "".join(sequences)



def RevComp(seq):
    replacements = str.maketrans("ACGT", "TGCA")
    return seq.translate(replacements)[::-1]


def Palindromes(seq):
    for i in range(4,13):
        for j in range(len(seq)-i+1):
            frame = seq[j:j+i]
            if frame == RevComp(frame):
                print(j+1, i, sep = ' ')
            else:
                pass

Palindromes(sequences)
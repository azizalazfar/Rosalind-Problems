import itertools


with open('rosalind_pper.txt') as handle:
    n,k = [int(x) for x in handle.read().split(' ')]
perms = list(itertools.permutations(range(n),k))
print(len(perms))
#with open('output_pper.txt') as outfile:
    #outfile.write(''.join(perms))


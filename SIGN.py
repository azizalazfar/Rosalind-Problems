import itertools
with open('rosalind_sign.txt') as file:
    n = int(file.read().strip('\n'))

pos = [str(i) for i in range(1,n+1)]
neg = [str(j) for j in range(-1,-(n+1),-1)]

diff = list(set(itertools.permutations(pos+neg, r = n)))

sign = []
for k in range(len(diff)):
    if len(set(list(abs(int(i)) for i in diff[k]))) == len(diff[k]):
        sign.append(list(diff[k]))

print(len(sign), '\n', '\n'.join(' '.join(x) for x in sign))
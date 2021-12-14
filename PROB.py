import math

with open('rosalind_prob.txt') as handle:
    candidate, A = handle.readline().strip('\n'), list(map(float, handle.readline().split(' ')))

def GC(text):
	count = 0
	for i in range(len(text)):
		if text[i] == 'G' or text[i] == 'C':
			count += 1
	return count

GC_count, AT_count = GC(candidate), len(candidate)-GC(candidate)
print(GC_count, AT_count)

B = []
for i in range(len(A)):
    B.append(math.log10(((1-A[i])/2)**AT_count * (A[i]/2)**GC_count))

print(' '.join(list(map(str, B))))

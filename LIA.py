######################################################### UNNECESSARY ######################################################
def nCr(n,r):
    from operator import mul
    from functools import reduce
    '''
    param: n and r = set of distinguishable outcomes/objects
    param: r = sample outcomes/objects
    returns = n!/(r!(n-r)!) for 0 < r < n 
    '''
    n_fact, nr_fact = reduce(mul, range(n, 0, -1),1), reduce(mul, range(n-r,0,-1),1)
    if r == 1:
        r_fact = 1
    elif r == 0:
        r_fact = 1
    else:
        r_fact = reduce(mul, range(r, 0, -1),1)
    
    return n_fact/(r_fact*nr_fact)

############################################################################################################################
from math import comb

with open('rosalind_lia.txt') as handle:
    k, N = list(map(int, handle.read().strip('\n').split(' ')))   # k = generation, N = successful AaBb organism
    p = 2**k        # total population of k generation

probability = 0
for i in range(N, p+1):
    prob = comb(p,i) * (0.75**(p-i)) * (0.25 ** i)
    probability += prob


print(round(probability, 3))
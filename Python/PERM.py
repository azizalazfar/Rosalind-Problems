import itertools
# with open('rosalind_perm.txt') as file:
#     n = file.read()
n = 6
sol =list(itertools.permutations([i for i in range(1, n+1)], n))
# for elem in sol:
#     for i in elem:
#         print(i, end = ' ')
#     print()


    
    
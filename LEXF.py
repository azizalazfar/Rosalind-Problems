import itertools

with open('rosalind_lexf.txt') as handle:
    symbols, n = ''.join(handle.readline().strip('\n').split(' ')), int(handle.readline())
    print(symbols,n)


products = list(itertools.product(''.join(symbols), repeat = n))
product_list = [''.join(nmer) for nmer in products]



with open('output_lexf.txt', 'w') as outfile:
    for nmer in product_list:
        outfile.write(nmer+'\n')
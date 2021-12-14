with open('rosalind_lexv.txt') as handle:
    symbols = handle.readline().strip('\n').split(' ')
    n = int(handle.readline().strip('\n'))


Lex = []
def LexV(L, word, n):
    if len(word) <= n and len(word) != 0:
        Lex.append(word)
    if L == n:
        Lex.append(word)
    else:
        for i in range(len(symbols)):
            LexV(L+1, word + symbols[i], n)

LexV(0, '', n)

Lex = list(set(Lex))

with open('output_lexv.txt', 'w') as outfile:
    outfile.write('\n'.join(sorted(Lex, key = lambda word:[symbols.index(c) for c in word])))

with open('rosalind_iprb.txt') as file:
	data = file.read().split(' ')

k,m,n = int(data[0]),int(data[1]),int(data[2])
p = k+m+n
Pr_X = 1- ((n/p)*(n-1)/(p-1) + (n/p)*(m/(p-1)*0.5) + (m/p)*(n/(p-1)*0.5) + (m/p)*(m-1)/(p-1)*0.25)

print(Pr_X)
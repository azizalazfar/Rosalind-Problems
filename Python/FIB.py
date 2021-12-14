def WascallyWabbits(n,k):
	child, adult = 1, 0
	for i in range(n - 1):
		child, adult = adult*k, adult + child
		
	return child+adult


print(WascallyWabbits(5,3))
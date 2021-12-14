def Hammdist(txt1, txt2):
	distance = 0
	for i in range(len(txt1)):
		if len(txt1) != len(txt2):
			print('patterns are not equal in length, you dumbfuck!')
		elif txt1[i] != txt2[i]:
			distance += 1
	return distance

with open('rosalind_hamm.txt') as f:
	file = f.read()
	file = list(file.splitlines())

print(Hammdist(file[0], file[1]))			

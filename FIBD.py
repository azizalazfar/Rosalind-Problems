# with open('test.txt') as file:
# 	data = file.readline().split()
# 	n,m = int(data[0]), int(data[1])
n,m = 6,3
fibo= []
child, adult = 1, 0
for i in range(0,n):
    child, adult = adult , adult+child 
    fibo.append(child+adult)
print(fibo)
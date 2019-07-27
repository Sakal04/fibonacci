x = [1, 1]
nx = [int(i) for i in x]
n = 10
while len(nx) < n:
	elem = sum(nx[-2:])
	nx.append(elem)
print(nx)

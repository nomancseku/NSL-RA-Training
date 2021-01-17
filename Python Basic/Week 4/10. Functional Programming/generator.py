def noman():
	a = 5
	for i in range(a):
		yield i


for i in noman():
	print(i)

	
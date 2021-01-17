def oddNumbers(n):
	for i in range(n):
		if i%2 != 0:
			yield i

print(list(oddNumbers(100)))
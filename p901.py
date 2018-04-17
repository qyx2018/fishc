for i in range (100,1000):
	sum = ((i % 10) ** 3) + (((i / 10) % 10) ** 3) + ((i / 100) ** 3)
#	print(sum)
	if sum == i:
		print(i)
	else:
		continue

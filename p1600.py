def min(x):
	least = x[0]
	print('least = ', least)
	for each in x:
		print("each = ", each)
		if each < least:
			print(111)
			least = each
	
	return least

print(min('5123456789'))
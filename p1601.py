def sum(x):
	result = 0

	for each in x:
#		print(each)
		if (type(each) == int) or (type(each) == float):
			result += each
#			print(result, each)
		else:
			continue
	
	return result
	
print(sum([1 ,2.1,2.3,'a','1',True]))
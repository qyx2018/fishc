def Dec2Bin(dec):
	temp = []
	result = ''
	
	while dec:
		quo = dec % 2
		dec = dec // 2
		temp.append(quo)
		
#	print(temp)
	while temp:
		result += str(temp.pop())
#		print(str(temp.pop()))
		
	return result
	
print(Dec2Bin(62))
#Dec2Bin(62)
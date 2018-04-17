def findStr(desStr, subStr):
	count = 0
	length = len(desStr)
	if subStr not in desStr:
		print('Did not find!')
	else:
		for each1 in range(length - 1):
			if desStr[each1] == subStr[0]:
				if desStr[each1+1] == subStr[1]:
					count += 1
		
		print('Total number is: %d' % count)
		
desStr = raw_input('Input your str: ')
subStr = raw_input('Input your substr: ')
findStr(desStr, subStr)
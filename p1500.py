q = True
while q:
	num = raw_input('Please input an int number(Q to quit): ')
	if num != 'Q':
		num = int(num)
		print('Shijinzhi -> Shiliujinzhi: %d -> 0x%x' %(num, num))
		print('Shijinzhi -> Bajinzhi: %d -> 0o%o' %(num, num))
		print('Shijinzhi -> Erjinzhi: %d ->' %num, bin(num))
	else:
		q = False
temp = raw_input('input year: ')
while not temp.isdigit():
	print('Wrong input, input again.')
	temp = raw_input('input year:')

year = int(temp)

#if year/400 == int(year/400):
if year%400 ==0:
	print(temp + ' is runnian.')
else:
#	if (year/4 == int(year/4)) and (year/100 != int(year/100)):
	if (year%4 == 0 and year%100 != 0):
		print(temp + ' is runnian!')
	else:
		print(temp + ' is not runnian.')
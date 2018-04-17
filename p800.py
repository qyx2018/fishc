score = int(raw_input('please input a number: '))
if 80 > score >= 60:
	print('C')
elif 90 > score >= 80:
	print('B')
elif 60 > score >= 0:
	print('D')
elif 100 >= score >= 90:
	print('A')
else:
	print('Error!')

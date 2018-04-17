from __future__ import print_function
times = 3
password = 'dabaicai'
print('------------------------------------')
print('Input password: ')

while times:
	guess = raw_input()
	if guess == password:
		print('Correct!')
		break
	elif '*' in guess:
		print('Do not include *', 'you have', times, 'chance.')
		continue
	else:
		print('Wrong', 'you have', times-1, 'chance.')
		times = times - 1

import random
times = 3
secret = random.randint(1,10)
print('------------------------------------')
guess = 0
print('Guess a number')
while (guess != secret) and (times > 0):
	temp = raw_input() #在python2.7中，raw_input与input有区别。返回的 object类型不同。只有当object的类型为 非int时，才可以使用isdigit（）函数。
	if temp.isdigit():
		guess = int(temp)
		times = times - 1
		if guess == secret:
			print ('Correct!!!')
		else:
			if guess > secret:
				print ('large than')
			else:
				print ('less than')
			if times > 0:
				print ('input again')
			else:
				print('no chance')
	else:
		print('Wrong input, please input again')
print ('gave over')
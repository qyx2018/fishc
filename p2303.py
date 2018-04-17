def age(n):
	if n == 1:
		return 10
	else:
		return age(n-1) + 2

print('Haha, I know, the fifth person is %d years old.' % age(5))
from __future__ import print_function # 用来去掉print输出后自动换行的问题。与 end 搭配使用即可实现。
temp = input('input a number: ')
number = int(temp)
while number:
	i = number - 1
	while i:
		print (' ', end = '')
		i = i -1
	j = number
	while j:
		print ('*', end = '')
		j = j - 1
	print()
	number = number - 1
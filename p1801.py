from __future__ import print_function
def Narcissus():
	for each in range(153, 1000):
		temp = each
		sum = 0
		while temp:
			sum = sum + (temp % 10) ** 3
			temp = temp // 10
			
		if sum == each:
			print(each, end = '\t')
			
print('The total number is: ', end = '')
Narcissus()
print()
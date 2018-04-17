def palindrome(string):
	list1 = list(string)
	list2 = reversed(list1)
	if list1 == list(list2):
		return 'Y'
	else:
		return 'N'

print(palindrome('abccba'))
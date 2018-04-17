def is_palindrome(n, start, end):
	if start > end:
		return 1
	else:
		return is_palindrome(n, start + 1, end - 1) if n[start] == n[end] else 0

string = raw_input('Please input string: ')
length = len(string) - 1

if is_palindrome(string, 0, length):
	print('\"%s" is back string' % string)
else:
	print('\"%s\" is not back string' % string)
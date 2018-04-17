symbols = r'''`@#$%^&*()_+-=/*{}[]|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

passwd = raw_input('Please input your password: ')

#Length
length = len(passwd)

while (passwd.isspace() or length == 0):
	passwd = raw_input('Your input is space or empty, please re-enter: ')
	length = len(passwd)
	
if length <= 8:
	flag_len = 1
elif 8 <= length < 16:
	flag_len = 2
else:
	flag_len = 3
	
flag_con = 0

# To see if it include symbols
for each in passwd:
	if each in symbols:
		flag_con = 1
		break

# To see if it include chars
for each in passwd:
	if each in symbols:
		flag_con += 1
		break

# To see if it include nums
for each in passwd:
	if each in symbols:
		flag_con += 1
		
# Print result
while 1:
	print('Your password level is: ')
	if flag_len == 1 or flag_con == 1:
		print('Low')
	elif flag_len == 2 or flag_con == 2:
		print('Middle')
	else:
		print('High')
		print('Please keep!')
		break
	
	print('Please use the following method to improve your password level: \n\
	\t1. Password must include with numbers, chars and symbols\n\
	\t2. Password must start with chars\n\
	\t3. Password must greater than 16.')
	break
	
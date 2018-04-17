from __future__ import print_function
print('|---- welcome!|')
print('|1: query|')
print('|2: insert|')
print('|3: delete|')
print('|4: quit|')

contacts = dict()

while 1:
	instr = int(raw_input('\n Please input code: '))
	
	if instr == 1:
		name = raw_input('Please input name: ')
		if name in contacts:
			print(name + ' : ' + contacts[name])
		else:
			print('Your input name is not included.')
	
	if instr == 2:
		name = raw_input('Please input name: ')
		if name in contacts:
			print('Your name is in the contacts -- >> ', end = '')
			print(name + ' : ' + contacts[name])
			if raw_input('update info(Y/N): ') == 'YES': contacts[name] = raw_input('Please input phone number: ')
		else:
			contacts[name] = raw_input('Please input phone number: ')
		
	if instr == 3:
		name = raw_input('Please input name: ')
		if name in contacts:
			del(contacts[name])
		else:
			print('Your input name is not included.')
			
	if instr == 4:
		break
		
print('|--- Thanks for using sys.|')
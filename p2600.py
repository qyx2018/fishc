user_data = {}

def new_user():
	prompt = 'Please input username: '
	while True:
		name = raw_input(prompt)
		if name in user_data:
			prompt = 'username in use, please re-enter a username: '
			continue
		else:
			break
			
	passwd = raw_input('Please input password: ')
	user_data[name] = passwd
	print('Successful! Please try to use username & password.')
	
def old_user():
	prompt = 'Please input username: '
	while True:
		name = raw_input(prompt)
		if name not in user_data:
			prompt = 'Your username is not existed, please re-enter: '
			continue
		else:
			break

	passwd = raw_input('Please input password: ')
	pwd = user_data.get(name)
	if passwd == pwd:
		print('Welcome to sys.')
	else:
		print('Password incorrect')
		
def showmenu():
	prompt = '''
|--- Create new account: N/n ---|
|--- Log on account: E/e ---|
|--- Quit: Q/q ---|
|--- Input code: '''

	while True:
		chosen = False
		while not chosen:
			choice = raw_input(prompt)
			if choice not in 'NnEeQq':
				print('Code error, please re-enter code: ')
			else:
				chosen = True
				
		if choice == 'q' or choice == 'Q':
			break
		if choice == 'n' or choice == 'N':
			new_user()
		if choice == 'e' or choice == 'E':
			old_user()
			
showmenu()
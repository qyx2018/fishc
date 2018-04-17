def file_write(file_name):
	f = open(file_name, 'w')
	print('Please input text\':w\' to quit and exit: ')
	
	while True:
		write_some = raw_input()
		if write_some != ':w':
			f.write('%s\n' % write_some)
		else:
			break
			
	f.close()
	
file_name = raw_input('Please input file name: ')
file_write(file_name)
from __future__ import print_function
def file_view(file_name, line_num):
	print('\nFile %s \'s behind of %s context is: \n' %(file_name, line_num))
	f = open(file_name)
	for i in range(int(line_num)):
		print(f.readline(), end = '')
		
	f.close()
	
file_name = raw_input(r'Please input the file name (c:\\test.txt):')
line_num = raw_input('Please input behind of line: ')
file_view(file_name, line_num)
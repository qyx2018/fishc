from __future__ import print_function
def file_view(file_name, line_num):
	if line_num.strip() == ':':
		begin = '1'
		end = '-1'
	
	(begin, end) = line_num.split(':')
	
	if begin == '':
		begin = '1'
	if end == '':
		end = '-1'
		
	if begin == '1' and end == '-1':
		prompt = '\'s full text'
	elif begin == '1':
		prompt = 'From the begining to %s' % end
	elif end == '-1':
		prompt = 'From %s to the end' % end
	else:
		prompt = 'From %s to %s.' %(begin, end)
	
	print('\n File %s%s include:\n' %(file_name, prompt))
	
	begin = int(begin) - 1
	end = int(end)
	lines = end - begin
	
	f = open(file_name)
	
	for i in range(begin):
		f.readline()
		
	if lines < 0:
		print(f.read())
	else:
		for j in range(lines):
			print(f.readline(), end = '')
	
	f.close()
	
file_name = raw_input(r'Please input file name: ')
line_num = raw_input('Please input lines number: ')
file_view(file_name, line_num)
def file_compare(file1, file2):
	f1 = open(file1)
	f2 = open(file2)
	count = 0
	differ = []
	
	for line1 in f1:
		line2 = f2.readline()
		count += 1
		if line1 != line2:
			differ.append(count)
	
	
	f1.close()
	f2.close()
	return differ
	
file1 = raw_input('Please input the first file name: ')
file2 = raw_input('Please input the second file name:')

differ = file_compare(file1, file2)

if len(differ) == 0:
	print('They are the same!')
else:
	print('They have %d difference:' % len(differ))
	for each in differ:
		print('The %d line is not the same.' % each)
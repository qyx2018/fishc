def file_replace(file_name, rep_word, new_word):
	f_read = open(file_name)
	
	content = []
	count = 0
	
	for eachline in f_read:
		if rep_word in eachline:
			count = eachline.count(rep_word)
			eachline = eachline.replace(rep_word, new_word)
		content.append(eachline)
		
	decide = raw_input('\n File %s with %s numbers %s \n, are you sure to instead  all % s with % s?\n YES?NO:' % (file_name, count, rep_word, rep_word, new_word))
	
	if decide in ['YES', 'Yes', 'yes']:
		f_write = open(file_name, 'w')
		f_write.writelines(content)
		f_write.close()
		
	f_read.close
	
file_name = raw_input('Please input file name: ')
rep_word = raw_input('Please input the instad stringsL: ')
new_word = raw_input('Please input the new word: ')
file_replace(file_name, rep_word, new_word)
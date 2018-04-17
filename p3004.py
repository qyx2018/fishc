import os

def print_pos(key_dict):
	keys = key_dict.keys()
	keys = sorted(keys)
	for each_key in keys:
		print('Keywords in the %s, %s.' %(each_key, str(key_dict[each_key])))
		
def pos_in_line(line, key):
	pos = []
	begin = line.find(key)
	while begin != -1:
		pos.append(begin + 1)
		begin = line.find(key, begin + 1)
		
	return pos
	
def search_in_file(file_name, key):
	f = open(file_name)
	count = 0
	key_dict = dict()
	
	for each_line in f:
		count += 1
		if key in each_line:
			pos = pos_in_line(each_line, key)
			key_dict[count] = pos
			
	f.close()
	return key_dict
	
def search_files(key, detail):
	all_files = os.walk(os.getcwd())
	txt_files = []
	
	for i in all_files:
		for each_file in i[2]:
			if os.path.splitext(each_file)[1] == '.txt':
				each_file = os.path.join(i[0], each_file)
				txt_files.append(each_file)
				
	for each_txt_file in txt_files:
		key_dict = search_in_file(each_txt_file, key)
		if key_dict:
			print('========================================================')
			print('In file [%s], found keyword [%s]' % (each_txt_file, key))
			if detail in ['YES', 'Yes', 'yes']:
				print_pos(key_dict)
				
key = raw_input('Please put this script in the folder you are looking for, input keywords: ')
detail = raw_input('Need to print keyword %s location (YES/NO): ' % key)
search_files(key, detail)
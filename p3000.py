import os

all_files = os.listdir(os.curdir)
type_dict = dict()

for each_file in all_files:
	if os.path.isdir(each_file):
		type_dict.setdefault('folder', 0)
		type_dict['folder'] += 1
	else:
		ext = os.path.splitext(each_file)[1]
		type_dict.setdefault(ext, 0)
		type_dict[ext] += 1
		
for each_type in type_dict.keys():
	print('There are %s types, with file %d.' %(each_type, type_dict[each_type])) 
import sys, os

default_file_loc = 'C:/Users/Ian/Documents/temp_py_help.txt'

def make_help_txt(searchterm, file = default_file_loc):
	orig_stdout = sys.stdout
	f = open(file, 'w')
	sys.stdout = f
	help(searchterm)
	sys.stdout = orig_stdout
	f.close()
	
if __name__ == '__main__':
	make_help_txt(sys.argv[1])
	os.system('start '+default_file_loc)
#	os.remove(default_file_loc)
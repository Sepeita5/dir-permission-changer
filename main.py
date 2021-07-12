#this program changes every directory's permission from a specified directory into user = read,write,execute; group = read,-,execute; other = read,-,execute.

import os
import subprocess

dir = input("Please Enter a Directory: ")
def dir_finder(path):
	directories = []
	for item in os.listdir(path):
		if os.path.isfile(item):
			continue
		if not item.startswith('.'):
			directories.append(item)
	return directories

dir_list = dir_finder(dir)

os.chdir(dir)
for directory in dir_list:
	subprocess.call(['chmod', 'u=rwx,og=rx', directory])




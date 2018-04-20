from utils import *

password = "lhlgmjmkmglqlompmoltmglilqlmlgmh"
bits_string = strtobits(password)
print(bits_string)
string = ''
for i in range(0,16):
	string += chr(int(bits_string[i*8:(i+1)*8],2))

print(string)
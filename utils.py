import itertools
import os
from string import maketrans
import random


IP = [
	58,50,42, 34,26,18,10,2,
	60,52,44,36,28,20,12,4,
	62,54, 46, 38, 30, 22, 14,6,
	64, 56, 48, 40,32,24, 16, 8,
	57, 49, 41, 33,25,17, 9,1,
	59, 51,43,35,27,19,11,3,
	61,53,45,37,29,21,13, 5,
	63,55, 47,39,31,23,15,7
]

# /* REVERSE PERMUTATION (RFP) */

RFP = [
	8,40,16,48,24,56,32,64,
	7, 39,15,47,23,55,31,63,
	6,38,14,46,22,54,30,62,
	5,37,13,45, 21,53,29,61,
	4,36,12,44,20,52,28,60,
	3, 35, 11,43,19,51,27,59,
	2, 34, 10, 42,18, 50,26,58,
	1,33,9,41, 17, 49, 25,57,
]

# /* E BIT_SELECTION TABLE */

E = [
	32, 1, 2, 3, 4, 5,
	4, 5,6, 7, 8, 9,
	8, 9, 10, 11, 12, 13,
	12, 13, 14, 15, 16, 17, 
	16, 17, 18, 19, 20, 21, 
	20, 21, 22, 23, 24, 25, 
	24, 25, 26, 27, 28, 29,
	28, 29, 30, 31, 32, 1
]


# /* PERMUTATION FUNCTION P */
P = [
	16, 7, 20, 21, 
	29, 12, 28, 17,
	1, 15, 23, 26,
	5, 18, 31,10,
	2, 8, 24, 14,
	32, 27, 3, 9,
	19, 13, 30, 6,
	22, 11, 4, 25,
]


# /* Inverse of P */
INV_P = [
	9, 17, 23, 31,
	13, 28, 2, 18,
	24, 16, 30, 6,
	26, 20, 10, 1,
	8, 14, 25, 3,
	4, 29, 11, 19,
	32, 12, 22, 7,
	5, 27, 15, 21,
]

intab = "0123456789abcdef"
outtab="fghijklmnopqrstu"

trantab = maketrans(intab, outtab)
reversetranstab = maketrans(outtab,intab)
# str = "this is string example....wow!!!"
# print str.translate(trantab)

def get64bits():
	# bitList = []
	x=''
	for i in range(0, 64):
		x = x+str(random.randint(0, 1))
		# bitList.append(x);
	print x;
	return x;

def bitsToStr(bitlist):
	temp=''
	for i in range(8):
		temp = temp+ format(int(bitlist[i*8:(i+1)*8],2),'02x')
	return temp.translate(trantab)	
def strtobits(str):
	bitlist=''
	temp =str.translate(reversetranstab)
	print temp
	for i in range((len(temp))/2):
		bitlist=bitlist+"{0:08b}".format(16*intab.index(temp[2*i])+intab.index(temp[2*i+1]))
	return bitlist

a = bitsToStr(get64bits())
print a
print strtobits(a)

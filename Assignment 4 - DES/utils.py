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

IPINV = [
	40, 8, 48, 16, 56, 24, 64, 32,
	39, 7, 47, 15, 55, 23, 63, 31,
	38, 6, 46, 14, 54, 22, 62, 30,
	37, 5, 45, 13, 53, 21, 61, 29,
	36, 4, 44, 12, 52, 20, 60, 28,
	35, 3, 43, 11, 51, 19, 59, 27,
	34, 2, 42, 10, 50, 18, 58, 26,
	33, 1, 41, 9, 49, 17, 57, 25
	]
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
RFPINV = [
	57, 49, 41, 33, 25, 17, 9, 1,
	59, 51, 43, 35, 27, 19, 11, 3,
	61, 53, 45, 37, 29, 21, 13, 5,
	63, 55, 47, 39, 31, 23, 15, 7,
	58, 50, 42, 34, 26, 18, 10, 2,
	60, 52, 44, 36, 28, 20, 12, 4,
	62, 54, 46, 38, 30, 22, 14, 6,
	64, 56, 48, 40, 32, 24, 16, 8
	]
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
S = [[], [], [], [], [], [], [], [], []]
S[1] = [14, 4, 13, 1, 2, 15, 11, 8, 3 , 10, 6, 12, 5, 9, 0, 7,0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,4, 1 , 14, 8, 13, 6, 2, 11, 15, 12, 9, 7,3, 10, 5, 0,15, 12, 8,2,4, 9, 1,7 , 5, 11, 3, 14, 10, 0, 6, 13 ,]
S[2] = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0,5, 10,3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,0, 14, 7, 11, 10, 4, 13, 1, 5, 8,12, 6, 9, 3, 2, 15,13, 8, 10, 1, 3, 15, 4, 2,11,6, 7, 12, 0,5, 14, 9,]
S[3] = [ 10, 0, 9,14,6,3,15,5, 1, 13, 12, 7, 11, 4,2,8, 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1, 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12,5, 10, 14, 7, 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12, ]
S[4] = [ 7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9, 10, 6, 9, 0, 12, 11, 7, 13, 15, 1 , 3, 14, 5, 2, 8, 4, 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14, ]
S[5] = [ 2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, 14, 11,2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6, 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3, ]
S[6] = [ 12, 1, 10, 15, 9, 2, 6,8, 0, 13, 3, 4, 14, 7, 5, 11, 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8, 9, 14, 15, 5, 2,8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13, ]
S[7] = [ 4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1, 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6, 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12, ]
S[8] = [ 13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12,7, 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2, 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8, 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11, ]

Keymap=[24, 27, 21, 6, 11, 15,13, 10, 25, 16, 3, 20,5, 1, 22, 14, 8, 18,26, 17, 9, 2, 23, 12,51, 34, 41, 47, 29, 37,40, 50, 33, 55, 43, 30,54, 31, 49, 38, 44, 35,56, 52, 32, 46, 39, 42,]
intab = "0123456789abcdef"
outtab="fghijklmnopqrstu"

trantab = maketrans(intab, outtab)
reversetranstab = maketrans(outtab,intab)


def get64bits():
	# bitList = []
	x=''
	for i in range(0, 64):
		x = x+str(random.randint(0, 1))
		# bitList.append(x);
	# print x;
	return x;

def bitsToStr(bitlist):
	temp=''
	for i in range(8):
		temp = temp+ format(int(bitlist[i*8:(i+1)*8],2),'02x')
	return temp.translate(trantab).lstrip()	
def strtobits(str):
	bitlist=''
	temp =str.translate(reversetranstab)
	# print temp
	for i in range((len(temp))/2):
		bitlist=bitlist+"{0:08b}".format(16*intab.index(temp[2*i])+intab.index(temp[2*i+1]))
	return bitlist.lstrip()
def xorbitlists(x,y):
	xor=''
	for a,b in zip(x,y):
		xor=xor+str(int(a)^int(b))
	return xor.lstrip()

def listPermuatate(permutationarray,bitlist):
	permutedlist=''
	for i in range(len(bitlist)):
		permutedlist=permutedlist+bitlist[permutationarray[i]-1]
	return permutedlist.lstrip()
def expansion(bitlist):
	expandedlist=''
	for i in range(48):
		expandedlist=expandedlist+bitlist[E[i]-1]
	return expandedlist.lstrip()
def splitList(bitlist):
	half=len(bitlist)/2
	return bitlist[:half].lstrip(),bitlist[half:].lstrip()
def sboxoutput(bitlist,boxnum):
	row =int(bitlist[0]+bitlist[5],2)
	col=int(bitlist[1]+bitlist[2]+bitlist[3]+bitlist[4],2)
	return "{0:04b}".format(S[boxnum][row*16+col])
inputxor='0100000000001000000000000000000000000100000000000000000000000000'
# inputxor = '0000000000100000000000000000100000000000000000000000010000000000'
# inputxor='0100000001011100000000000000000000000100000000000000000000000000'
# inputxor='0000000010000000100000100000000001100000000000000000000000000000'
# xor = [ 0x40, 0x5C, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00 ]
zerosboxes=[2,5,6,7,8]
# zerosboxes=[1,2,4,5,6]
# zerosboxes=[1,2,5,6,7,8]
# zerosboxes=[1,7,8]

inverse_inpxor=listPermuatate(IPINV,inputxor)
def inputPairs():
	f = open("inputpairs.txt", 'w+')
	for i in range(1000):
		ip1=get64bits()
		ip2=xorbitlists(ip1,inverse_inpxor)
		print >>f,bitsToStr(ip1),bitsToStr(ip2)
	f.close()

# print inverse_inpxor
# print listPermuatate(IP,inverse_inpxor)
# a = bitsToStr(get64bits())
# print a
# # print strtobits(a)
# a= get64bits()
# print a[:32]
# print expansion(a[:32])
# inputPairs()
# if(xorbitlists(strtobits('qsssmfqirrnpinrr'),strtobits('qsssufpirrnpmnrr'))==inverse_inpxor):
# 	print "asdfghjkl"
def findkey():
	partialfinalsboxkey = {
		1: 20,
		2: 27,
		4: 46,
		5: 34,
		6: 20,
		7: 37,
		8: 5,
		}
	mainkey=[]
	for i in range(56):
		mainkey.append('X')		
	for sboxes in partialfinalsboxkey:
		sboxkey="{0:06b}".format(partialfinalsboxkey[sboxes])
		for i,b in enumerate(sboxkey):
			mainkey[Keymap[(sboxes-1)*6+i]-1]=b
	return ''.join(mainkey)

def keysgenerator():
	f= open("keys.txt", 'w+')
	partialkey = list(findkey())
	# print findkey()
	unknownplaces = []
	for i in range(len(partialkey)):
		if partialkey[i]=='X':
			unknownplaces.append(i)

	boom = [ ['0', '1'] for _ in range(14) ]
	for replacement in itertools.product(*boom):
		kk = partialkey[:]
		for i in range(14):
			kk[unknownplaces[i]] = replacement[i]
		bitstring = ''.join(map(lambda x: str(x), kk))
		print >>f,bitstring 
	f.close()
# def generateKeys(key_arr):
# 	try:
# 		indices=key_arr.index('X')
# 	except ValueError:
# 		# print str(key_arr)
# 		print(''.join(key_arr))
# 	else:
# 		key_arr[indices]='0'
# 		generateKeys(key_arr)
# 		key_arr[indices]='1'
# 		generateKeys(key_arr)
# # key =XX1XX1XXX10X0X00XXX10XX01X1X1000001X01000100X10X0110X110
# key =['X', 'X', '1', 'X', 'X', '1', 'X', 'X', 'X', '1', '0', 'X', '0', 'X', '0', '0', 'X', 'X', 'X', '1', '0', 'X', 'X', '0', '1', 'X', '1', 'X', '1', '0', '0', '0', '0', '0', '1', 'X', '0', '1', '0', '0', '0', '1', '0', '0', 'X', '1', '0', 'X', '0', '1', '1', '0', 'X', '1', '1', '0']
# generateKeys(key)		
# findkey()

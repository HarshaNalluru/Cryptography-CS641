import itertools
import os
from string import maketrans
import random

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

def splitList(bitlist):
	half=len(bitlist)/2
	return bitlist[:half].lstrip(),bitlist[half:].lstrip()


# inverse_inpxor=listPermuatate(IPINV,inputxor)
def inputPairs():
	f = open("inputpairs.txt", 'w+')
	for i in range(1000):
		ip1=get64bits()
		ip2=xorbitlists(ip1,inverse_inpxor)
		print >>f,bitsToStr(ip1),bitsToStr(ip2)
	f.close()
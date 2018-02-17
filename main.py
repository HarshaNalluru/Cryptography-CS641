from utils import *
counter={}
f = open("input_output_pairs_1000.txt")
j=0
while True:
	j+=1;
	line = f.readline()
	if(not line):
		break
	ip1,op1=line.split("	")
	line = f.readline()
	ip2,op2=line.split("	")

	op1 = strtobits(op1)
	op2 = strtobits(op2)
	l1,r1=splitList(listPermuatate(RFPINV,op1))
	l2,r2=splitList(listPermuatate(RFPINV,op2))
	op_xor=xorbitlists(op1,op2)
	op_xor=listPermuatate(RFPINV,op_xor)
	l_xor,r_xor=splitList(listPermuatate(RFPINV,op_xor))
	delta35_xor=listPermuatate(INV_P,xorbitlists(r_xor,inputxor[32:]))

	el1=expansion(l1)
	el2=expansion(l2)
	for i in zerosboxes:
		if i not in counter:
			counter[i]={}
		for k in range(64):
			k= "{0:06b}".format(k)
			delta5_xor =xorbitlists(sboxoutput(xorbitlists(el1[(i-1)*6:i*6],k),i),sboxoutput(xorbitlists(el2[(i-1)*6:i*6],k),i))
			if(delta5_xor==delta35_xor[(i-1)*4:i*4]):
				if k not in counter[i]:
					counter[i][k]=1
				else:
					counter[i][k]+=1

	print j

f.close()
print counter





# print IPINV
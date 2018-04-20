chi_inv = [None]*32
for val in range(0,32):
	a = format(val, '05b')
	out =  [None]*5
	for x in range(0,5):
		out[x] = int(a[x]) ^ ( (int(a[(x+1)%5]) ^ 1) & int(a[(x+2)%5]) )
	out_val = int(str(out[0])+str(out[1])+str(out[2])+str(out[3])+str(out[4]), 2)
	chi_inv[out_val] = a

for val in range(0,8):
	a = format(val, '05b')
	a1 = format(val + 8, '05b')
	a2 = format(val + 16, '05b')
	a3 = format(val + 24, '05b')
	print(a, chi_inv[val],"  " ,a1, chi_inv[val+8], "  " ,a2, chi_inv[val+16], "  ", a3, chi_inv[val+24] )


	
		# print(x)
	# print( a,  format(chi_inv[val], '05b'))
	# a = "{0:b}".format(val)
	# print(out_val)
PC1 = [
  57, 49, 41, 33, 25, 17, 9,
  1, 58, 50, 42, 34, 26, 18,
  10,  2, 59, 51, 43, 35, 27,
  19, 11,  3, 60, 52, 44, 36,
  63, 55, 47, 39, 31, 23, 15, 
  7, 62, 54, 46, 38, 30, 22, 
  14,  6, 61, 53, 45, 37, 29, 
  21, 13,  5, 28, 20, 12,  4
]
shifts = [
1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]

# /* PERMUTED CHOICE 2 (PC@) */

PC2 = [
  14, 17, 11, 24,  1, 5, 
  3, 28 ,15,  6, 21, 10, 
  23, 19, 12,  4, 26, 8, 
  16,  7, 27, 20, 13, 2, 
  41, 52, 31, 37, 47, 55, 
  30, 40, 51, 45, 33, 48, 
  44, 49, 39, 56, 34, 53, 
  46, 42, 50, 36, 29, 32
]
CD={}
KS={}
for i in range(56):
  CD[i] = i


for i in range(8):
  for j in range(shifts[i]):
    t1=CD[0]
    t2=CD[28]
    for k in range(27):
      CD[k]=CD[k+1]
      CD[k+28]=CD[k+29]
      CD[27] = t1;
      CD[55] = t2;
  for k in range(48):
    if not i in KS:
      KS[i]={}
    if not k in KS[i]:
      KS[i][k]=CD[PC2[k]-1]

for i in KS[5]:
  print KS[5][i],
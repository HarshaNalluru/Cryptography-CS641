import time
from sage.crypto.util import bin_to_ascii


##----------------------------------------Main Coppersmith Attack Function-------------------------------------------------    

def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):
    """
    Coppersmith revisited by Howgrave-Graham
    finds a solution if:
    * b|modulus, b >= modulus^beta , 0 < beta <= 1
    * |x| < XX
    """
    dd = pol.degree()
    nn = dd * mm + tt
    # checks
    if not 0 < beta <= 1:
        raise ValueError("beta should belongs in (0, 1]")

    if not pol.is_monic():
        raise ArithmeticError("Polynomial must be monic.")

    # Coppersmith revisited algo for univariate
    # change ring of pol and x

    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)
    
    # construct lattice B
    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial    
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    # factor polynomial
    potential_roots = new_pol.roots()
    # print "potential roots:", potential_roots

    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    return roots

##----------------------------------------Helper Function-------------------------------------------------    
def strToInt(k):
    bin = BinaryStrings()
    ccc = bin.encoding(k)
    return int(str(ccc), 2)
##---------------------------------------Parameter Declaration--------------------------------------------

length_N = 1024  # size of the modulus
Kbits = 200      # size of the root
e = 5
N = 90861646124264969076247659324816928011765416103817759776108942310270353722886293373789498617747601273832759054599817416958027196159243140420149188323820910064519884642943554274386665061863223799713634977022573118004095436210289594592747581643668331636012215542467748413499016657610311519500523204995393504991
ZmodN = Zmod(N);
C = 51406844401277859213523204135383743220066806685218673631220904671159985888990492674708587474294983572509101851682650858629740803994916477956408308036107041373191165616632606546336872773281997776034486941145380800344067015344553230742191151587270125543983802440749401673330246885089966747945004168438760257338
pad = "Gupt_Nashak: This door has RSA encryption with exponent 5 and the password is "


##------------------------------TEST WHETHER THE FUNCTIONS WORK---------------------------------------------
#passw = 'Trump is the best'
# C = ZmodN(strToInt(pad+passw))^e

##------------------------------LOOP OVER THE LENGTH OF MESSAGE AND CHECK------------------------------------

for l in range(6, 200):
    bin = BinaryStrings()
    print(l)
    padding = int(str(bin.encoding(pad)) + "0"*l, 2)
    # print len(padding)
    P.<x> = PolynomialRing(ZmodN) #, implementation='NTL')
    pol = (padding + x)^e - C
    dd = pol.degree()

    beta = 1                                # b = N
    epsilon = beta / 20                      # <= beta / 7
    mm = ceil(beta**2 / (dd * epsilon))     # optimized value
    tt = floor(dd * mm * ((1/beta) - 1))    # optimized value
    XX = ceil(N**((beta**2/dd) - epsilon))  # optimized value

    roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)
    if roots != []:
        print("Found roots for l", l, "which are", roots)
        for root in roots:
            print(len(str(bin.encoding(pad)) + "0"*l))
            print(bin_to_ascii(Integer(root).binary()))
        break

##--------------------------------------Convert to ASCII--------------------------------------------------------
print(bin_to_ascii('0001101000100000011000110110110001110100010001100111100101101011011001100110011101010100011011100110110001011001'))


# 529908721024455254664710156348505
import time
from sage.crypto.util import *

debug = False

# display matrix picture with 0 and X
def matrix_overview(BB, bound):
    for ii in range(BB.dimensions()[0]):
        a = ('%02d ' % ii)
        for jj in range(BB.dimensions()[1]):
            a += '0' if BB[ii,jj] == 0 else 'X'
            a += ' '
        if BB[ii, ii] >= bound:
            a += '~'
        print a

def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):
    """
    Coppersmith revisited by Howgrave-Graham
    
    finds a solution if:
    * b|modulus, b >= modulus^beta , 0 < beta <= 1
    * |x| < XX
    """
    #
    # init
    #
    dd = pol.degree()
    nn = dd * mm + tt

    #
    # checks
    #
    if not 0 < beta <= 1:
        raise ValueError("beta should belongs in (0, 1]")

    if not pol.is_monic():
        raise ArithmeticError("Polynomial must be monic.")

    #
    # calculate bounds and display them
    #
    """
    * we want to find g(x) such that ||g(xX)|| <= b^m / sqrt(n)
    * we know LLL will give us a short vector v such that:
    ||v|| <= 2^((n - 1)/4) * det(L)^(1/n)
    * we will use that vector as a coefficient vector for our g(x)
    
    * so we want to satisfy:
    2^((n - 1)/4) * det(L)^(1/n) < N^(beta*m) / sqrt(n)
    
    so we can obtain ||v|| < N^(beta*m) / sqrt(n) <= b^m / sqrt(n)
    (it's important to use N because we might not know b)
    """
    if debug:
        # t optimized?
        print "\n# Optimized t?\n"
        print "we want X^(n-1) < N^(beta*m) so that each vector is helpful"
        cond1 = RR(XX^(nn-1))
        print "* X^(n-1) = ", cond1
        cond2 = pow(modulus, beta*mm)
        print "* N^(beta*m) = ", cond2
        print "* X^(n-1) < N^(beta*m) \n-> GOOD" if cond1 < cond2 else "* X^(n-1) >= N^(beta*m) \n-> NOT GOOD"
        
        # bound for X
        print "\n# X bound respected?\n"
        print "we want X <= N^(((2*beta*m)/(n-1)) - ((delta*m*(m+1))/(n*(n-1)))) / 2 = M"
        print "* X =", XX
        cond2 = RR(modulus^(((2*beta*mm)/(nn-1)) - ((dd*mm*(mm+1))/(nn*(nn-1)))) / 2)
        print "* M =", cond2
        print "* X <= M \n-> GOOD" if XX <= cond2 else "* X > M \n-> NOT GOOD"

        # solution possible?
        print "\n# Solutions possible?\n"
        detL = RR(modulus^(dd * mm * (mm + 1) / 2) * XX^(nn * (nn - 1) / 2))
        print "we can find a solution if 2^((n - 1)/4) * det(L)^(1/n) < N^(beta*m) / sqrt(n)"
        cond1 = RR(2^((nn - 1)/4) * detL^(1/nn))
        print "* 2^((n - 1)/4) * det(L)^(1/n) = ", cond1
        cond2 = RR(modulus^(beta*mm) / sqrt(nn))
        print "* N^(beta*m) / sqrt(n) = ", cond2
        print "* 2^((n - 1)/4) * det(L)^(1/n) < N^(beta*m) / sqrt(n) \n-> SOLUTION WILL BE FOUND" if cond1 < cond2 else "* 2^((n - 1)/4) * det(L)^(1/n) >= N^(beta*m) / sqroot(n) \n-> NO SOLUTIONS MIGHT BE FOUND (but we never know)"

        # warning about X
        print "\n# Note that no solutions will be found _for sure_ if you don't respect:\n* |root| < X \n* b >= modulus^beta\n"
    
    #
    # Coppersmith revisited algo for univariate
    #

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

    # display basis matrix
    if debug:
        matrix_overview(BB, modulus^mm)

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

    # 
    return roots

# https://github.com/mimoo/RSA-and-LLL-attacks/blob/master/coppersmith.sage

length_N = 1024  # size of the modulus
# Kbits = 8*30      # size of the roots
e = 5

n = 117000590783638097134264529188190097675001928712814587634422477724713032382551264043765949665540838462591176725973661879259079787867382797630539175380522220790542692376727339083646806110463030467703482124437653965084748517771565590230437979102397806761898570435861320186616734636726930132568539071750732836767
n_bits = n.digits(2)
z = Integer(n_bits, base=2)
if z == n:
    print "Hahahaa"
# Integer(str(ascii_to_bin(" cltFykfgTnlY")), base=2)
# message with X:s replaced with \x00
passage_message = "Descrifardo: This door has RSA encryption with exponent 5 and the password is "
passage_message_bin = ascii_to_bin(passage_message)
passage_message_bin_len = len(passage_message_bin)
# print passage_message_bin_len

# f = file('output_2.txt','a')
# f.write(str(a))
# f.close()
# load("main.sage")
# passage_message_bin_str = ''.join(str(e) for e in passage_message_bin_len)
# print type(passage_message_bin)
# passage_message_bin = str(passage_message_bin) + "000"
# print passage_message_bin

    
for k_bits in range(300):
    print k_bits
    m2 = Integer(str(passage_message_bin) + "0"*k_bits, base=2)
    # print m2
    f = file('output_roots_right.txt','a')
    f.write("m2 = "+str(m2)+"\n")
    c = 55127372485143185118477977875759360987939105298255623273291078476647124390200192168191805431399040264511285732135425834978033390160442898674372536810749500925899530559795236959138511319349966727845983354658163974982655683337730491153237831768713782444074338443975225788850945480558591673592805096460218140605

    N = n
    ZmodN = Zmod(n);
    M = ZmodN(m2)
    C = ZmodN(c)

    P.<x> = PolynomialRing(ZmodN) 
    # pol = ((M + x)**e - C).monic()
    pol = ((x + M)**e - C)
    dd = pol.degree()

    beta = 1                                # b = N
    epsilon = beta / 12                      # <= beta / 7
    mm = ceil(beta**2 / (dd * epsilon))     # optimized value
    tt = floor(dd * mm * ((1/beta) - 1))    # optimized value
    XX = ceil(N**((beta**2/dd) - epsilon))  # optimized value






    roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)
    # print hex(roots[0]).strip("0x").strip("L").decode("hex")
    # print roots
    f.write("root = "+str(roots)+"\n\n")
    f.close()
    if roots:
        rev_pass = ''
        password = Integer(roots[0]).binary()
        print password
        for set_8 in range(len(password)):
            rev_pass += password[len(password)-1-set_8]
        print rev_pass
        rev_pass = "0"*3+rev_pass
        print bin_to_ascii(rev_pass)
        break

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
    print "potential roots:", potential_roots

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

# length_N = 1024  # size of the modulus
# # Kbits = 8*30      # size of the roots
# e = 5

# # n = 17128253199894018356121352721813384810490073007249104944917185889284458477972764510189878223087898232323989051389196334498213309997968573900259909767276527308390944053199244416237135384010089907191097552095732629493007104656712229046898881071816439581052398074559706748835744846278126604658780761748930367026870270721107608579738966885369180506986732756678936607083412698682076417247965156736007257325263626024309893180725648019322055002425052139312236077136949139163190290260407572716784894091812931974782646175099495402465049210759703810960600180113684855659892187079557217272929145318759442388534032426335197492209
# n = 117000590783638097134264529188190097675001928712814587634422477724713032382551264043765949665540838462591176725973661879259079787867382797630539175380522220790542692376727339083646806110463030467703482124437653965084748517771565590230437979102397806761898570435861320186616734636726930132568539071750732836767
# n_bits = n.digits(2)
# z = Integer(n_bits, base=2)
# if z == n:
#     print "Hahahaa"
# # Integer(str(ascii_to_bin(" cltFykfgTnlY")), base=2)
# # message with X:s replaced with \x00
# passage_message = "Descrifardo: This door has RSA encryption with exponent 5 and the password is"
# passage_message_bin = ascii_to_bin(passage_message)
# passage_message_bin_len = len(passage_message_bin)
# # print passage_message_bin_len

# # f = file('output_2.txt','a')
# # f.write(str(a))
# # f.close()
# # load("main.sage")
# # passage_message_bin_str = ''.join(str(e) for e in passage_message_bin_len)
# # print type(passage_message_bin)
# # passage_message_bin = str(passage_message_bin) + "000"
# # print passage_message_bin

    
# for k_bits in range(300):
#     m2 = Integer(str(passage_message_bin) + "0"*k_bits, base=2)
#     print m2
#     f = file('output_roots_right.txt','a')
#     f.write("m2 = "+str(m2)+"\n")
#     # m2 = 115187245656325575698875729790282642212930548748463092065204369418708216291155665989205021047468838142025051843099835931219635476459638358291768944024977260201839742782124859088529873971905522340780587673634963892906501655934652033065483105959124652995675375187226593058645297329744588405060727900047060073362881226582222539170913146258434555654371489139229050690663311680730101709133573886961243713446437623231124732560606386944666112685417134293162413492709060639338136519444676948426963320805588894438876123699208985971986627457388344748617780375247355235008512
#     c = 55127372485143185118477977875759360987939105298255623273291078476647124390200192168191805431399040264511285732135425834978033390160442898674372536810749500925899530559795236959138511319349966727845983354658163974982655683337730491153237831768713782444074338443975225788850945480558591673592805096460218140605

#     N = n
#     ZmodN = Zmod(n);
#     M = ZmodN(m2)
#     C = ZmodN(c)

#     P.<x> = PolynomialRing(ZmodN) 
#     # pol = ((M + x)**e - C).monic()
#     pol = ((x + M)**e - C)
#     dd = pol.degree()

#     beta = 0.5                                # b = N
#     epsilon = beta / 7                      # <= beta / 7
#     mm = ceil(beta**2 / (dd * epsilon))     # optimized value
#     tt = floor(dd * mm * ((1/beta) - 1))    # optimized value
#     XX = ceil(N**((beta**2/dd) - epsilon))  # optimized value






#     roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)
#     # print hex(roots[0]).strip("0x").strip("L").decode("hex")
#     print roots
#     f.write("root = "+str(roots)+"\n\n")
#     f.close()
# # print len(roots[0])
# a = roots[0].digits(2)
# print a
# c = bin_to_ascii(a)
# print c
rev_pass = ''
password = '011010100001001001000010110100100101001000010010011011101101011001010110000101100000010001011'
for set_8 in range(len(password)):
    rev_pass += password[len(password)-1-set_8]
print rev_pass
print(bin_to_ascii('000'+rev_pass))
# 000110100010000001101000011010100110101101110110010010000100101001001011010000100100100001010110
# 8085788970795186269987162198


# 011010100001001001000010110100100101001000010010011011101101011001010110000101100000010001011
# 000011010100001001001000010110100100101001000010010011011101101011001010110000101100000010001011
# \rBHZJBM\xda\xca\xc2\xc0\x8b
# BHZJBMdacac2c08b
# print len(c)
# ############################################
# # Test on Stereotyped Messages
# ##########################################    

# print "//////////////////////////////////"
# print "// TEST 1"
# print "////////////////////////////////"

# # RSA gen options (for the demo)
# length_N = 1024  # size of the modulus
# Kbits = 200      # size of the root
# e = 3

# # RSA gen (for the demo)
# p = next_prime(2^int(round(length_N/2)))
# q = next_prime(p)
# N = p*q
# ZmodN = Zmod(N);

# # Create problem (for the demo)
# K = ZZ.random_element(0, 2^Kbits)
# Kdigits = K.digits(2)
# M = [0]*Kbits + [1]*(length_N-Kbits); 
# for i in range(len(Kdigits)):
#     M[i] = Kdigits[i]
# M = ZZ(M, 2)
# C = ZmodN(M)^e

# # Problem to equation (default)
# P.<x> = PolynomialRing(ZmodN) #, implementation='NTL')
# pol = (2^length_N - 2^Kbits + x)^e - C
# dd = pol.degree()

# # Tweak those
# beta = 1                                # b = N
# epsilon = beta / 7                      # <= beta / 7
# mm = ceil(beta**2 / (dd * epsilon))     # optimized value
# tt = floor(dd * mm * ((1/beta) - 1))    # optimized value
# XX = ceil(N**((beta**2/dd) - epsilon))  # optimized value

# # Coppersmith
# start_time = time.time()
# roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)

# # output
# print "\n# Solutions"
# print "we want to find:",str(K)
# print "we found:", str(roots)
# print("in: %s seconds " % (time.time() - start_time))
# print "\n"

# ############################################
# # Test on Factoring with High Bits Known
# ##########################################
# print "//////////////////////////////////"
# print "// TEST 2"
# print "////////////////////////////////"

# # RSA gen
# length_N = 1024;
# p = next_prime(2^int(round(length_N/2)));
# q = next_prime( round(pi.n()*p) );
# N = p*q;

# # qbar is q + [hidden_size_random]
# hidden = 200;
# diff = ZZ.random_element(0, 2^hidden-1)
# qbar = q + diff; 

# F.<x> = PolynomialRing(Zmod(N), implementation='NTL'); 
# pol = x - qbar
# dd = pol.degree()

# # PLAY WITH THOSE:
# beta = 0.5                             # we should have q >= N^beta
# epsilon = beta / 7                     # <= beta/7
# mm = ceil(beta**2 / (dd * epsilon))    # optimized
# tt = floor(dd * mm * ((1/beta) - 1))   # optimized
# XX = ceil(N**((beta**2/dd) - epsilon)) # we should have |diff| < X

# # Coppersmith
# start_time = time.time()
# roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)

# # output
# print "\n# Solutions"
# print "we want to find:", qbar - q
# print "we found:", roots
# print("in: %s seconds " % (time.time() - start_time))
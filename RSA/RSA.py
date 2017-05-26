import random
import binascii

"********* MILLER RABIN *******************************************"
def Miller_Rabin(num, a):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    v = pow(a, s, num)
    if v != 1:  # this test does not apply if v is 1.
        i = 0
        while v != (num - 1):
            if i == t - 1:

                return False
            else:
                i = i + 1
                v = (v ** 2) % num
    return True



def TraceMiller_Rabin(num, a):

    print("\n\t=== Check if {0} may be prime or not (Miller Rabin) ===".format(num))
    print("\tn = {0}, a = {1}".format(num, a))
    s = num - 1
    print("\ts = n - 1 = {0}".format(s))
    t = 0
    print("\tt = 0")
    while s % 2 == 0:
        s = s // 2
        print("\ts = s / 2 = {0}".format(s))
        t += 1
        print("\tt = t + 1 = {0}".format(t))

    v = pow(a, s, num)
    print("\tv = (a ^ s) mod n = {0}".format(v))

    if v != 1:  # this test does not apply if v is 1.
        i = 0
        print("\ti = 0")
        while v != (num - 1):
            print("\tv is not n - 1")
            if i == t - 1:
                print("\tcheck(i = t - 1)")
                print("\t{0} NOT PRIME.".format(num))
                return

            else:
                i = i + 1
                v = (v ** 2) % num
                print("\ti = i + 1 = {0}".format(i))
                print("\tv = (v ^ 2) mod n = {0}".format(v))
    print("\t{0} PERHAPS PRIME.".format(num))

def mb_test(x):
    for test in range(20):  # print once
        a = random.randrange(1, x - 1)
        if not Miller_Rabin(x, a):
            return False
    return True

"************************************************************************"
def getRandomPrime():
    a = []
    b = []
    for genbits in range (0,5):
        a = []
        for i in range(32):
            a.append(random.randint(0,1)) # 2: means get rid of 0b >>> bin(6)[2:] '110'
        print "b_" + str(genbits) + str(a)
        y = a[31]
        b.append(y)

    b.insert(0, 1)
    b.insert(6, 1)
    print "7 bits: " + str(b)
    x = ''.join(map(str,b))
    x = int(x,2) #OUR PRIME NUMBER
    for e in range(25):
        b.insert(0,0)
    print "Number:" + str(x) + " " + str(b)

    a = random.randrange(1, x - 1)

    if mb_test(x):
        print TraceMiller_Rabin(x,a)
        return x
    else:
        print TraceMiller_Rabin(x,a)


"********* GCD AND EXTENDED EUCLIDEAN ALGORITHM **************************"
def gcd(a,b):

    if ((a % b) == 0):
        return b
    else:
        return gcd(b, a % b)




def euclidean_algorithm(r1, r2):
    r = r1 % r2

    if gcd(r1, r2) == 1:
        q = r1 // r2
        origR2 = r2
        s = 0
        s1 = 1
        t = 1
        t1 = 0

        print('%-5s%-5s%-5s%-5s%-5s%-5s' % ("q", "r1", "r2", "r", "si", "ti"))
        print("----------------------------")
        while r2 != 0:

            r = r1 % r2

            q = r1 // r2
            print('%-5i%-5i%-5i%-5i%-5i%-5i' % (q, r1, r2, r, s1, t1))
            r1 = r2
            r2 = r

            temp = t

            t = t1 - q * t
            t1 = temp

            temp = s

            s = s1 - q * s
            s1 = temp

        if s1<0:
            s1 += origR2
        q = " "
        r= " "
        r2 = " "
        print('%-5s%-5i%-5s%-5s%-5i%-5i' % (q, r1, r2, r, s1, t1))
        return t1

    else :
        print('%-5s%-5s%-5s%-5s%-5s%-5s' % ("q", "r1", "r2", "r", "si", "ti"))
        print("----------------------------")
        q = r1//r2
        r = r1 % r2
        s1 = 1
        t1 = 0
        print('%-5s%-5i%-5s%-5s%-5i%-5i' % (q, r1, r2, r, s1, t1))

"****** ENCRYPT/DECRYPT *******************************************************"

def encrypt(msg,e,n):
    #  c = m**e % n
    encrypt = fast_exponentiation(msg,e,n)

    return encrypt

def decrypt(cmsg, d, n):
    # cmsg = c**d %n
    decrypt = fast_exponentiation(cmsg,d,n)
    return decrypt

"***** FAST EXPONENTIATION******************************************************"
def fast_exponentiation(base,power,modn):
    y = 1
    a = []
    power = bin(power)
    a = power[2:]
    for i in power:
        if  i == '0':
            y = y * y % modn
        else:
            if i == '1':
                y = y * base *y % modn

    return y


def add_zeros(binary):
    while len(binary) < 32:
        binary = "0" + binary
    return binary

def inverse_value(phin):
    e = 3

    while e < 9999999:
        print "e = " + str(e);
        t1 = euclidean_algorithm(phin,e)
        if (t1):
            d = t1 #the inverse
            break
        else:
            e = e + 1
    return t1,e

def p_q():
    p = getRandomPrime()

    q = getRandomPrime()

    while (p == None):
        p = getRandomPrime()
    while (q == None):
        q = getRandomPrime()

    print "p = " + str(p)
    print "q = " + str(q)
    n = p * q
    print "n = " + str(n)
    return p,q,n


def main():


    p,q,n = p_q()

    phi = (p-1)*(q-1)
    print "phin = " + str(phi)


    d,e = inverse_value(phi) #if d is negative and computing a d such that (d*e) mod phi = 1
    d = d % phi;             # because often got a negative d..normalized it
    if (d < 0):
        d += phi;



    print "\np = " + str(p), "q = " + str(q), "n = " + str(n), "e = " + str(e), "d = " + str(d)


    print "\np =",add_zeros(bin(p)[2:]), "\nq =",add_zeros(bin(q)[2:]), "\nn =",add_zeros(bin(n)[2:]),\
    "\ne =",add_zeros(bin(e)[2:]), "\nd = " + add_zeros(bin(d)[2:])


   # binaryMsg = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in msg), 0))


    #intMsg = int(binaryMsg,2)


    question = raw_input("\nwould you like to encrypt or decrypt? (1: encrypt 0: decrypt) \n")
    if(question =='1' ):
        msg = int(raw_input("\nenter number to encrypt " + "\n"))

        cmsg = encrypt(msg, e, n)
        decrypted = decrypt(cmsg, d, n)  # int number

        print "message is " + str(msg), "\nencrypted is " + str(cmsg),"\ndecrypted should be " + str(decrypted)
    elif(question =='0'):
        cmsg = int(raw_input("enter encrypted message "))
        d = int(raw_input("enter your 'd' "))
        n = int(raw_input("enter your 'n' (or mod) "))
        print "\nyour decrypted message is ",decrypt(cmsg,d,n)

   #m = ,  encrypted:1024, d=8141,n=10379



#######################################################
''' p1,q1,n1 = p_q()
    phin1 = (p - 1) * (q - 1)
    print "phin = " + str(phin1)

    d1, e1 = inverse_value(phin1)

    print "\np = " + str(p1), "q = " + str(q1), "n = " + str(n1), "e = " + str(e1), "d = " + str(d1)

    print "\np =", add_zeros(bin(p1)[2:]), "\nq =", add_zeros(bin(q1)[2:]), "\nn =", add_zeros(bin(n1)[2:]), \
        "\ne =", add_zeros(bin(e1)[2:]), "\nd = " + add_zeros(bin(d1)[2:])'''

#######################################################
main()


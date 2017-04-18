
def gcd(a, b):
    greatestDivisor = 0
    if a > b:  # 6 mod 5
        greatestDivisor = b
        for i in range(1, b):
            if a % i == 0 and b % i == 0:
                greatestDivisor = i  # if same divisor
    elif a == b:
        greatestDivisor = b
    else:  # a < b
        greatestDivisor = a
        for i in range(1, a):
            if a % i == 0 and b % i == 0:
                greatestDivisor = i
    return greatestDivisor




def euclidean_algorithm(r1, r2):
    r = r1 % r2

    if gcd(r1, r2) == 1:
        q = r1 // r2
        s = 1
        s1 = 0
        t = 0
        t1 = 1


        print('%-5s%-5s%-5s%-5s%-5s%-5s' % ("q", "r1", "r2", "r", "si", "ti"))
        print("----------------------------")
        while r2 != 0:

            r = r1 % r2

            q = r1 // r2
            print('%-5i%-5i%-5i%-5i%-5i%-5i' % (q, r1, r2, r, t1, s1))
            r1 = r2
            r2 = r

            temp = t

            t = t1 - q * t
            t1 = temp

            temp = s

            s = s1 - q * s
            s1 = temp
        q = " "
        r= " "
        r2 = " "
        print('%-5s%-5i%-5s%-5s%-5i%-5i' % (q, r1, r2, r, t1, s1))



print("Euclidean Algorithm (75,28)\n")

euclidean_algorithm(75,28)


R_1 = int(input("Enter R" + u'\u2081:'))
R_2 = int(input("Enter R" + u'\u2082:'))

euclidean_algorithm(R_1, R_2)



def fast_exponentiation(base,power,modn):
    y = 1
    while power > 0:
        if  power % 2 == 0:
            base = base * base % modn
            power = power/2
        else:
            power = power -1
            y = y * base % modn

    return y



def main():

    base = input("enter base: ")
    power = input("enter power ")
    modn = input("enter mod number ")
    print fast_exponentiation(base, power, modn)


main()
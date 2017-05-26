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



def main():

    base = input("enter base: ")
    power = input("enter power ")
    modn = input("enter mod number ")
    print fast_exponentiation(base, power, modn)


main()
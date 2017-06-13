pt_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ct_alph = 'DEFHIJKLMNOPQRSTUVWXYZABC'


def encrypt(key, plaintext):
    # initailize the ciphertext to an empty string.
    ciphertext = ''

    # iterate through over through each letter in the plaintext
    for letter in plaintext:
        # For any character which are not in thr alphabet
        # (spaces, punctuation, etc) keep them the way
        # they are.
        if letter not in pt_alph:
            ciphertext += letter
            continue

        # Get the index of the letter in the plaintext alphabet
        index = pt_alph.index(letter)

        # Find the letter in the cipher text alphabet at this
        # index, and add it to the ciphertext.

        index += key
        ciphertext += pt_alph[index]

        # + pt_alph[index]

        # pt_alph[key++];

    # Return the ciphertext.
    return ciphertext


def decrypt(key, cText):
    # initailize the ciphertext to an empty string
    ciphertext = ''

    # iterate through over through each letter in the plaintext
    for letter in cText:
        # For any character which are not in thr alphabet
        # (spaces, punctuation, etc) keep them the way
        # they are.
        if letter not in pt_alph:
            ciphertext += letter
            continue

        # Get the index of the letter in the plaintext alphabet
        index = pt_alph.index(letter)

        # Find the letter in the cipher text alphabet at this
        # index, and add it to the ciphertext.

        index -= key
        ciphertext += pt_alph[index]

    return ciphertext


def main():
    m = input("what would you like to encrypt? ")
    m = m.upper()
    k = input("What is the keyshift? ")

    secret_message = encrypt(k, m)
    print("The cipher message is: " + secret_message)

    """dkit = input("would you like to decrypt with the same key? (1/0)")
    if dkit == 1:

        secret_message = decrypt(k,secret_message)
        print("your original message was:" + secret_message)"""

    dk = input("would you like to decrypt a cipher? (1/0)")
    if dk == 1:
        cipher_message = input("what is the cipher text? ")
        cipher_message = cipher_message.upper()
        dk = input("what is the keyshift? ")
        secret_message = decrypt(dk, cipher_message)
        print("The original message was: " + secret_message)
    else:
        pass


main()


""" P2: One Time Pad Implementation
Authors:
Clarissa Podell,  Emplid# 23468450
Syeda Kazmi Shah, Emplid#
"""

import os
import sys


""" NOTE:
The primary data type used is a bytearray which is a sequence
of bytes interpreted as integers (the ASCII character set).
"""


def read_bytes_from_file(filename):
    """ Reads data from file and returns contents as a bytearray. """

    with open(filename, 'rb') as f: # 'b' binary stream yields bytes
        data = bytearray(f.read().rstrip('\n')) # remove newlines

    return data


def write_bytes_to_file(filename, data):
    """ Takes a filename and data as input and writes data to an output file. """

    with open(filename, 'w') as f:
        f.write(data)


def genkey(length):
    """ Gen key invokes /dev/urandom to generate an array of random bytes. """

    key = bytearray(os.urandom(length))

    # Write key to file named keyfile
    write_bytes_to_file('keyfile', key)


def enc():
    """ Enc reads plaintext from file and generates the key, then produces the
    ciphertext and writes the result to an output file.
    """

    # Read plaintext from file
    plaintext = read_bytes_from_file('plaintext')

    # Length of plaintext message
    n = len(plaintext)

    # Generate key based on length 'n' & write to file
    genkey(n)

    # Read key from file
    key = read_bytes_from_file('keyfile')

    # Generate ciphertext by performing a byte-by-byte XOR on each index of the
    # plaintext and key arrays until iteration reaches length 'n'
    ciphertext = bytearray( plaintext[i] ^ key[i] for i in range(n) )

    # Write ciphertext to file
    write_bytes_to_file('ciphertext', ciphertext)

    print '\nYour message has been encrypted and saved to file \'ciphertext\''


def dec(cipher_filename, key_filename):
    """ Dec reads ciphertext and key from files specified by user, then produces the
    original plaintext message and writes the result to an output file.
    """

    # Read ciphertext from file specified by user
    ciphertext = read_bytes_from_file(cipher_filename)

    # Read key from file specified by user
    key = read_bytes_from_file(key_filename)

    # Length of message
    n = len(ciphertext)

    # Generate original plaintext by performing a byte-by-byte XOR on each index
    # of the ciphertext and key arrays until the length 'n' is reached
    originalmsg = bytearray( ciphertext[i] ^ key[i] for i in range(n) )

    # Write the decrypted message to a file named original_message
    write_bytes_to_file('original_message', originalmsg)

    print '\nYour message has been decrypted:'

    return originalmsg


def delete(keyfile_name):
    """ Allows the user to delete the keyfile. """

    os.remove(keyfile_name)


def main():

    print 'Which operation would you like to perform?\n(1) Encrypt\n(2) Decrypt\n(3) Delete a keyfile'
    option = int(input())

    if option == 1:

        # Read plaintext message from user
        message = raw_input("Write your plaintext message:\n")

        # Create a file named plaintext & write the message to file
        write_bytes_to_file('plaintext', message)

        # Encrypt message
        enc()

    elif option == 2:

        # Prompt user for the ciphertext and key filenames
        cipher_file = raw_input("What is the name of your ciphertext file? ")
        key_file = raw_input("What is the name of your key file? ")

        # Decrypt message
        decrypted = dec(cipher_file, key_file)

        print '{:s}\n'.format(decrypted)

        # Let the user know whether or not cryptosystem was successful
        if decrypted == read_bytes_from_file('plaintext'):
            print 'Congratulations, you have a perfectly secret OTP cryptosystem!'
        else:
            print 'Sorry, your OTP cryptosystem was not successful.'

    elif option == 3:

        try:
            keyfile_name = raw_input("Enter name of key file that you would like to delete: ")
            delete(keyfile_name)
        except IOError:
            print "Error: File may not exist or is already deleted. Please try again."
            keyfile_name = raw_input("Enter name of key file that you would like to delete: ")
            delete(keyfile_name)

    else:
        # Invalid input (print error message and exit)
        sys.exit("Sorry, invalid input. Try again.")


if __name__ == '__main__':
    main()
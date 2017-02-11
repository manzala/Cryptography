pt_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ct_alph = 'DEFHIJKLMNOPQRSTUVWXYZABC'

def encrypt(plaintext):
    #initailize the ciphertext to an empty string
    ciphertext=''
    
    #iterate through over through each letter in the plaintext
    for letter in plaintext:
        #For any character which are not in thr alphabet
        #(spaces, punctuation, etc) keep them the way
        #they are.
        if letter not in pt_alph:
            ciphertext += letter
            continue
        
        #Get the index of the letter in the plaintext alphabet
        index = pt_alph.index(letter)
        
        #Find the letter in the cipher text alphabet at this
        #index, and add it to the ciphertext.
        ciphertext += ct_alph[index]
    
    #Return the ciphertext.
    return ciphertext

def main():
    m = input('what would you like to encrypt?')
    m = m.upper()
    
    secret_message = encrypt(m)
    
    print(secret_message)
    
main()

    
   
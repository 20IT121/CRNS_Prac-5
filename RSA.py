import sympy
import random
import math


p = sympy.randprime(999999 , 99999999)
q = sympy.randprime(999999 , 99999999)
if(q == p):
    q = sympy.randprime(999999 , 99999999)
n = p*q
z = (p-1)*(q-1) # phi(n)

## TODO Key generation Part

e = int(random.randint(2,z-1))  # public key
while(math.gcd(e,z) != 1):
    e = int(random.randint(2,z-1))

k = 1
while((1+k*z)%e != 0):
    k+=1
d = (1+k*z)/e

# print(d)

def encryption(value):
    result = (value**e)% n
    return result

def decryption(value):
    result = (value**d)% n
    return result

def ciphertextCharwise(m):
    cipher = ''
    for ch in m:
        cipher = cipher + chr((ord(ch) ** e) % n)
    return cipher

def decryptCipherCharwise(cipher):
    print(cipher)
    plain = ''
    for letter in cipher:
        plain = plain + chr( (int(cipher) ** d) % n)
    return plain

def char_by_char(m):
    cipherText = ciphertextCharwise(m)
    plainText = decryptCipherCharwise(cipherText)
    return plainText
    

def block_wise(block_size,m):
    size = len(m)
    while(size % block_size != 0):
        m = m + 'z'

    encryptedValue = []
    decryptedValue = []

# block wise splitting here 
    i = 0
    while(i <= size):
        cipher = ciphertextCharwise(m[i:i+block_size])
        encryptedValue.append(cipher)
        decryptedValue.append(decryptCipherCharwise(cipher))
        i += block_size
    return decryptedValue

def isBlockSize_Valid (block_size,m):
    text_size = len(m)
    if(block_size <= 1 or block_size >= text_size):
        return False
    return True

def main():
    m = input("Enter the plain text: ")

    print("\nEnter 1 if u want to encrypt character by character")
    print("Enter 2 if u want to encrypt your message block wise")
    option = int(input("\nEnter here :"))

    if(option == 1):
        decryptedValue = char_by_char(m)
    else:
        block_size = int(input("\nEnter the size of block: "))
        while(isBlockSize_Valid(block_size,m) == False):
            block_size = int(input("\nEnter the size of block: "))
        decryptedValues = block_wise(block_size,m)
        print(decryptedValues)

main()




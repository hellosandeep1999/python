# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:37:36 2020

@author: Sandeep
"""

import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2   
        x = x2- temp1* x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    n = p * q


    phi = (p-1) * (q-1)

    
    e = random.randrange(1, phi)

    
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = int.from_bytes(plaintext.encode('utf-8'), byteorder='big')
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = int.to_bytes(ciphertext, length=len(message), byteorder='big').decode('utf-8') 
    return ''.join(plain)
    

print("RSA Encrypter/ Decrypter")
p = int(input("Enter a prime number (17, 19, 23, etc): "))
q = int(input("Enter another prime number (Not one you entered above): "))
print("Generating your public/private keypairs now . . .")
public, private = generate_keypair(p, q)
print("Your public key is ", public ," and your private key is ", private)
message = input("Enter a message to encrypt with your private key: ")
encrypted_msg = encrypt(private, message)
print("Your encrypted message is: ")
print(''.join(map(lambda x: str(x), str(encrypted_msg))))
print("Decrypting message with public key ", public ," . . .")
print("Your message is:")
print(decrypt(public, encrypted_msg))





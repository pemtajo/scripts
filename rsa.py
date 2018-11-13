#!/usr/bin/python2
import sys, ast

from optparse import OptionParser

parser = OptionParser("usage: %prog [options]")
parser.add_option("-p", "--p", dest="p", action="store", default='223', help="Value of p prime")
parser.add_option("-q", "--q", dest="q", action="store",default='59', help="Value of q prime")
parser.add_option("-e", "--encrypt", dest="encrypt", action="store_true",default=False, help="Do operation encrypt")
parser.add_option("-d", "--decrypt", dest="decrypt", action="store_true",default=False, help="Do operation decrypt")
parser.add_option("-m", "--message", dest="message", action="store",default=None, help="Message for encrypted/decrypted")
parser.add_option("-k", "--key", dest="e", action="store",default='97', help="Number e, for prime relative with phi")

(options, args) = parser.parse_args()

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
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q, e):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    n = p * q
    phi = (p-1) * (q-1)

    if gcd(e, phi) != 1:
        raise ValueError('e must be relative prime with phi')

    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]

    return cipher

def decrypt(pk, ciphertext):
    key, n = pk

    try:
        plain = [chr(((char ** key) % n)) for char in ciphertext]
    except ValueError as error:
        print("It's not possible decrypt this text with there number of p,q and e!")
        exit(0)

    return ''.join(plain)
    
if __name__ == '__main__':
    encrypted_msg=None
    print ("RSA Encrypter/ Decrypter")
    print ("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(int(options.p), int(options.q), int(options.e))
    print ("Your public key is ", public ," and your private key is ", private)
    if(options.encrypt):
        if (options.message is None):
            message = raw_input("Enter a message to encrypt with your private key: ")
        else:
            message = options.message
        encrypted_msg = encrypt(private, message)
        print ("Your encrypted message is: ")
        print (encrypted_msg)
    
    if(options.decrypt):
        if (encrypted_msg is None):
            if(options.message is None):
                encrypted_msg = ast.literal_eval(raw_input("Enter a message to decrypt with your private key: "))
            else:
                encrypted_msg = ast.literal_eval(options.message)
        print ("Decrypting message with public key ", public ," . . .")
        print ("Your message is:")
        print (decrypt(public, encrypted_msg))
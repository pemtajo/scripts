#!/usr/bin/python

#using pycrypto
#script for encrypt

#

# ideua
# an mode ransom
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from optparse import OptionParser

import sys
sys.path.append("../..")

if len(sys.argv) < 3:
    print ("usage : mycry inputfile password")
    raise SystemExit


charUseless=' ' #blank space

class PlainText(object):
    """docstring for PlainText."""

    def __init__(self, arg, sizeBlock):
        super(PlainText, self).__init__()
        self.arg = arg
        self.sizeBlock=sizeBlock
        self._splitForSizeBlock()

    def _splitForSizeBlock(self):
        self.arg+=(self.sizeBlock-(len(self.arg)%self.sizeBlock))*charUseless
        self.blocks=[self.arg[i: i + self.sizeBlock] for i in range(0, len(self.arg), self.sizeBlock)]

SIZE_BLOCK=16


filename =sys.argv[1]
password= sys.argv[2]

obj=PlainText(filename, SIZE_BLOCK)

print(obj.blocks)


hash=SHA256.new()
hash.update(password)



encrypter= AES.new('This is a key123', AES.MODE_ECB)


for block in obj.blocks:
    cyphertext=encrypter.encrypt(block)
    print("TESTE: "+ cyphertext)



print(encrypter.decrypt(cyphertext))

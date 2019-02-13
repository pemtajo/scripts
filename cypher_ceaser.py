#!/usr/bin/python
# coding=UTF-8
# encoding=UTF-8

import sys

def apply_rotation(c, factor):
    if c.isalpha():
        lower = ord('A') if c.isupper() else ord('a') #ASCII value - to count starting him
        c = chr(lower + ((ord(c) - lower + factor) % 26))
    return c

def caesar_cipher(s, k):
    new_message = ''
    factor = k % 26
    for c in s:
        new_message += apply_rotation(c, factor)
    return new_message

if len (sys.argv) != 3 :
    print "Usage: "+sys.argv[0]+" text factor"
    sys.exit (1)

print (caesar_cipher(sys.argv[1], int(sys.argv[2])))
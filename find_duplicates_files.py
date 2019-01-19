#!/usr/bin/python
# coding=UTF-8
# encoding=UTF-8


#Script to find duplicate files, even with diff names
# The output is a tuple wih
# the first item is the duplicate file
# the second item is the original file

import sys
import os
import hashlib
import time
import datetime

hashs=[]
root=os.path.expanduser('~/')
duplicate=[]

#Function to read file data and calcule hash md5
def calculateMD5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).digest()

def foundHash(hash):
    for h in hashs:
        if h[0] == hash:
            return h[1]
    return None

def addTuple(tuple):
    if(returnDateCreation(tuple[0])<returnDateCreation(tuple[1])):
        duplicate.append([tuple[1], tuple[0]])
        return
    
    duplicate.append(tuple)

def addHash(tuple):
    hashs.append(tuple)

def returnDateCreation(file):
    return datetime.datetime.strptime(time.ctime(os.path.getctime(file)), '%a %b %d %H:%M:%S %Y')
#Run for all folders and calculate hash

def pass_folder(folder):
    files=[os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    folders= [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]
    
    for f in files:
        hash=calculateMD5(f)
        found=foundHash(hash)
        if found is None:
            addHash([hash, f])
        else:
            addTuple([f, found])

    for folder in folders:
        pass_folder(folder)

pass_folder(root)   

if not duplicate:
    print("Not duplicate file found!")
    exit()


print("Duplicate files found:")
for d in duplicate:
    print(str(d)+ '\n')

#!/usr/bin/python3
# coding=UTF-8
# encoding=UTF-8

def parentheses_matching(str):
    open = "({[" 
    closed = ")}]"
    i = []
    for c in str:
        if c in open:
            i.append(c) 
        elif c in closed:
            if not i:
                return False
            if closed.index(c) != open.index(i.pop()):
                return False 
    if not i:
        return True
    else:
        return False

print(parentheses_matching("([]"))

#!/usr/bin/python3
# coding=UTF-8

import sys

def fib(n):
    if n < 0:
        raise ValueError('Index was negative.')
    elif n in [0, 1]:
        return n

    m=[[1, 1], [1,0]]
    aux=m

    for _ in range(n-2):
        aux=mul(m, aux)
    
    return aux[0][0]

def mul(A,B):
    C = [[0 for row in range(len(A))] for col in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C

print("fib(0) = "+str(fib(0)))
print("fib(1) = "+str(fib(1)))
print("fib(2) = "+str(fib(2)))
print("fib(3) = "+str(fib(3)))
print("fib(4) = "+str(fib(4)))
print("fib(5) = "+str(fib(5)))
print("fib(6) = "+str(fib(6)))
print("fib(7) = "+str(fib(7)))
print("fib(8) = "+str(fib(8)))
print("fib(9) = "+str(fib(9)))
print("fib(10) = "+str(fib(10)))
print("fib(11) = "+str(fib(11)))
#!/usr/bin/python
# coding=UTF-8
# encoding=UTF-8


# You are given an array [1, 2, 3, 4, 5, 6, 7] and you have to add every last element to next to each iteration [1, 7, 2, 6, 3, 5, 4].
# /*
# outsideIn([1, 2, 3, 4, 5, 6, 7]) => [1, 7, 2, 6, 3, 5, 4]
# outsideIn(['a', 'b', 'c', 'd', '0', '8', 'i']) => ['a', 'i', 'b', '8', 'c', '0', 'd']
# */

def last_element_each_int(array):
    aux=array[:]
    for i in range((len(array)+1)/2):
        aux[i*2]=array[i]
        if((i*2)+1<len(array)): #avoid IndexError
            aux[(i*2)+1]=array[len(array)-1-i]

    return aux

def outsideIn(l):
    return [x for (a, b) in zip(l, l[::-1]) for x in (a, b)][:len(l)]

print(outsideIn([1, 2, 3, 4, 5, 6, 7]))
print(outsideIn(['a', 'b', 'c', 'd', '0', '8', 'i']))
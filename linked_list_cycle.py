#!/usr/bin/python
# coding=UTF-8

class LinkedListNode():

    def __init__(self, value):
        self.value=value
        self.next=None
        self.visited=False

def contains_cycle(list):
    while list.next is not None:
        if(list.next.visited):
            return True

        list.visited=True
        list=list.next
    
    return False

a = LinkedListNode(5)
b = LinkedListNode(1)
c = LinkedListNode(9)
d = LinkedListNode(9)

a.next = b
b.next = c
c.next = d
# d.next = b

print(contains_cycle(a))


#!/usr/bin/python
# coding=UTF-8
# encoding=UTF-8
import sys
import os
import hashlib
import time
import datetime

class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def size(self):
        return len(self.items)

class Queue(object):
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
    
    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if self.out_stack.size() == 0:

            # Move items from in_stack to out_stack, reversing order
            while self.in_stack.size() > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.push(newest_in_stack_item)

            # If out_stack is still empty, raise an error
            if self.out_stack.size() == 0:
                raise IndexError("Can't dequeue from empty queue!")

        return self.out_stack.pop()
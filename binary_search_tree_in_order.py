#!/usr/bin/python
# coding=UTF-8
# encoding=UTF-8

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right



def is_binary_search_tree(root):
    list_in_order = return_InOrder(root)
    for i in range(len(list_in_order)-1):
        if(list_in_order[i]>list_in_order[i+1]):
            return False
    
    return True
    
def return_InOrder(b):
    if b is None:
        return []
    
    return return_InOrder(b.left) + [b.value] + return_InOrder(b.right)
        


root = BinaryTreeNode(4)
root.insert_left(2)
root.insert_right(5)
root.left.insert_left(1)
root.left.insert_right(10)

print (is_binary_search_tree(root))

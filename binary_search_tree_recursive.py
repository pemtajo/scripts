#!/usr/bin/python
# coding=UTF-8
# encoding=UTF-8
  

#This implementation is wrong for some cases, for example, when a left leaf is bigger then the root value
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

    def is_binary_search_tree(self):
        if self.left is None and self.right is None:
            return True

        return self.is_left_balanced() and self.is_right_balanced()
    
    def is_left_balanced(self):
        if self.left is None:
            return True
        return self.left.value < self.value and self.left.is_binary_search_tree()

    def is_right_balanced(self):
        if self.right is None:
            return True
        return self.right.value > self.value and self.right.is_binary_search_tree()


root = BinaryTreeNode(4)
root.insert_left(2)
root.insert_right(5)
root.left.insert_left(1)
root.left.insert_right(10)

print (root.is_binary_search_tree())

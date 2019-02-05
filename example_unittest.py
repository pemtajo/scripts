#!/usr/bin/python3
# coding: utf-8

import unittest
from unittest import TestCase

class I(TestCase):
    def testOne(self):
        self.assertEqual(1, self._num)

class A(TestCase):
    _num=None
    _text=None
    def testTwo(self):
        self.assertIn('1', self._text)

class B(A, I):
    def __init__(self, obj):
        TestCase.__init__(self,obj)
        self._num=1
        self._text="I am Number 1"

class C(A):
    def __init__(self, obj):
        TestCase.__init__(self,obj)
        self._num=2
        self._text="I am not Number 1"

if __name__ == '__main__':
    unittest.main()
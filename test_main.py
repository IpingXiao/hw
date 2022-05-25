#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from unittest import main
from pythontest import count_vowels,count_vowels2
from unittest import TestCase


class Test(TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels('appleou'),4)

    def test_count_vowels2(self):
        self.assertEqual(count_vowels('china'), 2)

if __name__=='__main__':
    unittest.main()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 18:41:22 2020

@author: yangsong
"""


# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Follow up: Could you solve it without converting the integer to a string?

def isPalindrome(x):
    if x<0:
        return False
    else:
        x_letter=str(x)
        if x_letter==x_letter[::-1]:
            return True
        else:
            return False
    
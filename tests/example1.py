# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:29:29 2023

@author: willi
"""

# actual example here

from awkish import Awk

myawk = Awk()

@myawk.beginjob
def begin(nr):
    print("begin")

@myawk.begin
def beginfile(filename):
    print("\nbegin", filename)

@myawk.when(lambda f0: f0 != "")
def printline(fields):
    print(" ".join(fields), end="")

@myawk.when(lambda f2=1: int(f2) % 2 == 0)
def doline(nr, f2):
    # difference between fields[n] and fn is that fn is None if it
    # isn't there but fields[n] raises an exception.
    print(" ***", f2, nr, end="")

@myawk.when(lambda line: line != "")
def printend():
    # terminates a line
    print()

myawk.end
def end():
    print("\nend")

myawk("../tests/mawktest.txt", "../tests/mawktest.txt")
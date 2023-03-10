# -*- coding: utf-8 -*-
"""Practical 9 MCI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZSOVFoDEWz43ZWBsDsQ1sP6-xnjQTHXJ
"""

from scipy import array
from scipy.linalg import funm
from sympy import *
from numpy import *

m = array([[5,-2],[1,2]])
funm(m,lambda x: x**2 - 7*x +12)

M= Matrix([[2,0,0],[1,4,-1],[-2,-4,4]])
#M
print(M.eigenvects())

sym_eigenvects = []
for tup in M.eigenvects():
    for v in tup[2]:
        sym_eigenvects.append(list(v))

print(sym_eigenvects)

p=Matrix(sym_eigenvects)
p=p.transpose()
p

P_inverse = p.inv()
P_inverse

result = P_inverse*M
D=result*p
D

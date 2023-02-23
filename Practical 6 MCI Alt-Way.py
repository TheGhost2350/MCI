import numpy as np
import sympy as sp
from numpy import *

lst1=[]
order=int(input("Enter the Number of Rows of The Matrix:"))
order2=int(input("Enter the Number of Columns of The Matrix:"))

for i in range(order*order2):
    elements=int(input("Enter the Element for the Matrix:"))
    lst1.append(elements)
newmat=np.reshape(lst1,(order,order2))

print(newmat)
print()

R=sp.Matrix(newmat).rref()
rank=sp.Matrix(newmat).rank()

print("Row Reduced Form:\n",R)
print("Rank:",rank)
print()

cmsp=sp.Matrix(newmat).columnspace()
nsp=sp.Matrix(newmat).nullspace()

#shape=newmat.shape[1] #[1] for Columns & [0] for Rows.

transmat=newmat.transpose()


if len(cmsp)==0:
    print("No Column Space.")
else:
    print("Column Space:\n",cmsp)
print()
if len(nsp)==0:
    print("No Null Space.")
else:
    print("Null Space:\n",nsp)
print()
print("Transpose:\n",transmat)
print()

R2=sp.Matrix(transmat).rref()
rankt=sp.Matrix(transmat).rank()

print("Row Reduced Form of Transpose:\n",R2)
print("Rank of Transpose:",rankt)
print()

cmsp2=sp.Matrix(transmat).columnspace()
nsp2=sp.Matrix(transmat).nullspace()

if len(cmsp2)==0:
    print("No Row Space of Transpose.")
else:
    print("Row Space of Transpose:\n",cmsp)
print()
if len(nsp2)==0:
    print("No Left Null Space of Transpose.")
else:
    print("Left Null Space of Transpose:\n",nsp)
print()


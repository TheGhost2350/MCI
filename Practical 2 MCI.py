import numpy as np , sympy as sp

M1=np.matrix([[8,5,2],[3,3,1],[7,8,1]])
print("Matrix M1 is \n",M1)

a=sp.Matrix([[8,5,2],[3,3,1],[7,8,1]]).rref()
print("The Row Echelon Form is",a)

rank_M1=sp.Matrix([[8,5,2],[3,3,1],[7,8,1]]).rank()
print("The Rank Of Matrix is",rank_M1)

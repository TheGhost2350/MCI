import numpy as np,sympy
matrix=[]
row=int(input("Enter the number of rows:"))
column=int(input("enter the number of columns:"))
for i in range(row):
  a=[]
  for j in range(column):
    a.append(int(input("Enter element of matrix:")))
  matrix.append(a)
A=np.array(matrix)

n=A.shape[1]
print("Matrix A:{}\n".format(A))
B=A.transpose()
print("Matrix B:{}\n".format(B))
#null space and column space of A
nsp1=sympy.Matrix(A).nullspace()
csp1=sympy.Matrix(A).columnspace()
print("Null space:{}\n".format(nsp1))
print("column space:{}\n".format(csp1))                           
#left null space and ro space of a
nsp2=sympy.Matrix(B).nullspace()
csp2=sympy.Matrix(B).columnspace()
print("Left null space:{}\n".format(nsp2))
print("Row space:{}\n".format(csp2))

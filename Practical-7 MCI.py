from sympy import *
import numpy as np

rows=int(input("Enter No. of Rows:"))

cols=int(input("Enter No. of Columns:"))


matrix=[]

for i in range(rows):
    a=[]
    for j in range(cols):
        a.append(int(input("Enter Element of Matrix:")))
    matrix.append(a)
print(matrix)
mat=np.array(matrix)

print()
print("Entered Matrix:\n",mat)

deter=int(np.linalg.det(mat))

print()
print("Determinant of Matrix:",deter)
print()

if deter == 0:
    print("Matrix is Linearly Dependent.")
else:
    print("Matrix is Linearly Independent.")
    
print("For Linear Combinations")

k=int(input("Enter Value:"))
c=k*mat

print(c)

b=[]
print("Enter Vector 1")
p=int(input("Enter No. of Rows and the the Val:"))
for i in range(p):
    ele=int(input("Enter Value:"))
    b.append(ele)

print("Vector 1",b)

q=[]
print("Enter Vector 2 same len as of Vector 1")
r=int(input("Enter No. of Rows and the the Val:"))
for i in range(r):
    ele=int(input("Enter Value:"))
    q.append(ele)

print("Vector 2",q)

print("Linear Combinations:")
x=int(input("Enter Value 1:"))
z=int(input("Enter Value 2:"))

d=[]
for i in b:
    d.append(x*i)
print(d)
g=[]
for i in q:
    g.append(z*i)
print(g)

sum=[]
print("Linear Combination of Vector 1 and Vector 2:")
for i in range(len(q)):
    sum.append(d[i]+g[i])
print(sum)

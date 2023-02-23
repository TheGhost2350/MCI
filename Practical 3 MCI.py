import numpy as np
from numpy import *



k=int(input("Enter The Order of The Square Matrix:"))
m=int(input("Enter the Row For the Minor:"))
n=int(input("Enter the Column For the Minor:"))


if m>k:
    print("Number of Rows Cannot be more than The Given Matrix Order!!")
    exit() 
elif n>k:
    print("Number of Columns Cannot be more than The Given Matrix Order!!")
    exit()
        
m=m-1
n=n-1
   
matrix=[]
cf=[]
cof=[]

for i in range(k):
    a=[]
    for j in range(k):
        a.append(int(input("Enter Element of Matrix:")))
    matrix.append(a)

for i in range(k):
    for j in range(k):
        print(matrix[i][j],end=" ")
    print()

mat=matrix
delM=np.delete(mat,(m),axis=0)
delN=np.delete(delM,(n),axis=1)

print("The Minor Matrix of The Given Element is: \n",delN)
minor=linalg.det(delN)
print("Minor of The Given Element is:",minor)

if (m+n)%2!=0:
    cf.append((-1)*minor)
    
elif (m+n)%2==0:
    cf.append(minor)

def MINOR():

    m=int(input("Enter the Row For the Minor:"))
    n=int(input("Enter the Column For the Minor:"))

    m=m-1
    n=n-1
    
    mat=matrix
    delM=np.delete(mat,(m),axis=0)
    delN=np.delete(delM,(n),axis=1)

    print("The Minor Matrix of The Given Element is: \n",delN)
    minor=linalg.det(delN)
    print("Minor of The Given Element is:",minor)

    if (m+n)%2!=0:
        cf.append((-1)*minor)
       
    elif (m+n)%2==0:
        cf.append(minor)
        
print()
while True:
    ques=input("Do You want to Find Minor For Another Element(Y/N):")
    print()
    if ques=="y" or ques=="Y":
        MINOR()
        print()

    elif ques=="n" or ques=="N":
        print("Cofactors are:",cf)
        break

    else:
        print("Invalid Output!!")
        print()

cofactor=reshape(cf,(k,-1))
print("Adjoint of Matrix is: \n",cofactor.T)

deter=linalg.det(mat)
print("Determinant of Matrix is:",deter)

inv=(1/deter)*(cofactor.T)
print("Inverse of Matrix is: \n",inv)

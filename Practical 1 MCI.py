import numpy as np

#Entering List of Elements.
M1=np.matrix([[8,5,2],[3,3,1],[7,8,1]])
print("Matrix M1 is \n",M1)

#Taking User Inputs.
matrix=[]
row = int(input("Enter Number of Rows:"))
column = int(input("Enter Number of Columns:"))

for i in range(row):
  a=[]
  for j in range(column):
    a.append(int(input("Enter Element of Matrix:")))
  matrix.append(a)

c=np.reshape(matrix,(row,-1))
print("The Entered Matrix is: \n",c)

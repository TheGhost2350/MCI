import numpy as np

a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#encode matrix
ecm = [[3,4],[3,6]]


#lists of Alphabets and its values
smallalpha = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capitalalpha = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphavalues = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

#(1)
b ="India"
listb = list(b)
lenb = len(listb)
print("The Length of String is:",lenb)

#(2)
for i in range(lenb):
  for j in range(27):
    if(listb[i] == smallalpha[j]):
      a[i] = alphavalues[j]
      break
    elif(listb[i] == capitalalpha[j]):
      a[i] = alphavalues[j]
      break


if(lenb%2 == 1):
  lenb = lenb+1
a = a[0:lenb]
a

#convert this array to a 2D Array

c = np.reshape(a,(2,-1))
print("2D Numpy Array is: \n",c)

c = np.matmul(ecm,c)
c

# Convert to 1d array for displaying
k = 0
for i in range(2):
  for j in range(int(lenb/2)):
    a[k] = c[i][j]
    k = k+1
a = a[0:lenb]
print("Encoding Matrix:",ecm)
print("Encrypted Form:",a)

#Decoding
import numpy as np
from numpy.linalg import inv
#Initial Values
a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#Encoding Matrix
ecm=[[3,4],
     [3,6]]

#lists of Alphabets and its Values
smallalpha = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capitalalpha = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphavalues = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

# elements in Encrypted Matrix
lenb = 6
a=[63,46,12,81,48,12]

#convert array to 2d matrix for further multiplication with the inverse of Encoding Matrix

tdm= np.reshape(a,(2,-1))
tdm

dcm = inv(ecm)
print("Inverse of Encoded Matrix is: \n",dcm)
print()
dcm = np.matmul(dcm,tdm)
print(dcm)

# Convert to 1D array for extracting word
k=0
for i in range(2):
  for j in range(int(lenb/2)):
    a[k] = round(dcm[i][j])
    k = k+1
a

# Creating a decoded word
text = ""
for i in range(0,lenb):
  for j in range(0,27):
    if(a[i]==alphavalues[j]):
      text = "".join([text, smallalpha[j]])

print("Decoded Message:",text)

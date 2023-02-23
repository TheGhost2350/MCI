import numpy as np

m=np.matrix([[1+2j,2+3j,1-3j],[1-2j,7+8j,3+2j]])

h=m.conjugate()
print("Conjugate of Given Matrix: \n",h)

x=m.getH() #"getH()" Function for Conjugate Transpose
print("Conjugate Transpose of Given Matrix: \n",x)

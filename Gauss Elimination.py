import numpy as np
import sys

n=int(input("Enter Order of Matrix:"))
a=np.zeros((n,n+1))
x=np.zeros(n)

for i in range(n):
    for j in range(n+1):
        a[i][j]=float(input('a['+str(i)+']['+str(j)+']='))

for i in range(n):
    if a[i][i]==0:
        sys.exit("Division By Zero!!")
    for j in range(i+1,n):
        ratio=a[j][i]/a[i][i]
        for k in range(n+1):
            a[j][k]=a[j][k]=ratio*(a[i][k])

#Back Substitution.
x[n-1]=a[n-1][n]/a[n-1][n-1]
for i in range(n-2,-1,-1):
    x[i]=a[i][n]
    for j in range(i+1,n):
        x[i]=x[i]-a[i][j]*(x[j])
    x[i]=x[i]/a[i][i]

print("\nRequired Solution is: ")
for i in range(n):
    print(np.around(x[i],decimals=2))

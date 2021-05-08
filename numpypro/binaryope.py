import numpy as np 
a=np.array([[1,2],[3,4]])
b=np.array([[4,3],[2,1]])
print(a.T) #Transpose
#add arrays
print("Array sum:\n",a+b)
#multiply array
print("Array Multiplication:\n",a*b)
#matrix Multiplication
print("matrix Multiplication:\n",a.dot(b))
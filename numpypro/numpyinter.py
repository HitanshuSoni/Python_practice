import numpy as np 
x=np.zeros((2,2),dtype=[('x','i4'),('y','i4')])
print(x)
# creating array from list with type float
a=np.array([[1,2,3],[5,8,7]],dtype='float')
print("Array created using passed list:\n",a)
#creating array from tuple
b=np.array((1,2,3))
print("\nArray created using passed tuple:\n",b)
#creating 3x4 array with all zeros
c=np.zeros((3,4))
print("\nAn array initilized with all zeros:\n",c)
#create a constant value array of complex type
d=np.full((3,3),6,dtype='complex')
print("\nAn array initilized with all 6s.Array type is complex:\n",d)
#create an array with random values 
e=np.random.random((2,2))
print("\nA random array:\n",e)
#create a sequence of int
#from 0 to 30 with steps of 5
f=np.arange(0,30,5)
print("\nA sequential array with steps of 5:\n",f)
#create a sequence of 10 value in range 0 to 5
g=np.linspace(0,5,10)
print("\nA sequential array with 10 values between 0 and 5:\n",g)
#Reshaping 3x4 array to 2x2x3 array
arr=np.array([[1,2,3,4],[5,2,4,2],[1,2,0,1]])
newarr=arr.reshape(2,2,3)
print("\nOriginal array:\n",arr)
print("Reshaped array:\n",newarr)
#Flatten array
arr=np.array([[1,2,3],[4,5,6]])
flarr=arr.flatten()
print("\nOriginal array:\n",arr)
print("Flatten array:\n",flarr)
#create a 2x2 identity matrix
d=np.eye(2)
print("\n2x2 identity matrix:\n",d)
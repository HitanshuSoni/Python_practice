import numpy as np
#creating array obj
arr=np.array([[1,2,3],[5,6,7]])
#printing type of arr type
print("Array is of type: ",type(arr))
#print array dimension(axes)
print("No. of dimensions: ",arr.ndim)
#print shape of array
print("Shape of array: ",arr.shape)
#print size (total num of elements ) of array
print("Size of array: ",arr.size)
#print type of elelment in array
print("Array stored elements of type: ",arr.dtype)
#empty array
x=np.empty([3,2],dtype=int)
print(x)
#zero array
x=np.zeros(5 , dtype=np.int)
print(x)
#zero dtype
x=np.zeros((2,2),dtype=[('x','f'),('y','f')])
print(x)
import numpy as np 
a=np.array([[1,4,2],[3,4,6],[0,-1,5]])
#sorted array
print("Array elements in sorted order:\n",np.sort(a,axis=None))
#sort array row-wise
print("Row-wise sorted array:\n",np.sort(a,axis=1))
#specify sort algo..
print("Column wise sort by applying merge-sort:\n",np.sort(a,axis=0,kind='mergesort'))

#example to  show sorting of structured array
#set alias name for dtype
dtypes=[('name','S10'),('grad_year',int),('cgpa',float)]
#valus to be put in array
values=[('Hitanshu',2022,9.5),('Shivani',2022,9.8),('Ishan',2022,9.0),('Hunny',1999,10.0)]
#creating array
arr=np.array(values,dtype=dtypes)
print("\nArray sorted by names:\n",np.sort(arr,order='name'))
print("Array sorted by year of and then cgpa\n",np.sort(arr,order=['grad_year','cgpa']))
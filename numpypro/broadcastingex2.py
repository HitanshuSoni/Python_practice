import numpy as np 
a=np.arange(3).reshape((3,1))
b=np.arange(3)
a.shape=(3,1)
b.shape=(3,)
print(a+b)
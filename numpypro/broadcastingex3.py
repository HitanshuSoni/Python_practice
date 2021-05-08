import numpy as np 
M=np.ones((3,2))
a=np.arange(3)
M.shape=(3,2)
a.shape=(3,)
print(M+a[:,np.newaxis])
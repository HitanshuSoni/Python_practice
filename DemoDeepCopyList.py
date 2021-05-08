from copy import deepcopy
lst1=['a','b','c',['d','e']]
lst2=deepcopy(lst1)
lst2[1]='x'
lst2[3][0]='h'
print(lst1)
print(lst2)

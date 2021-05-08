lst1=['a','b','c',['d','e']]
lst2=lst1[:]
lst2[1]='x'
lst2[3][0]='h'
print(lst1)
print(lst2)

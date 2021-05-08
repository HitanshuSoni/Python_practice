lst1=[10,20,30,40,50]
lst2=lst1
print(lst1,lst2)
print(id(lst1),id(lst2))
lst2[1]=99
print(lst1,lst2)
print(id(lst1),id(lst2))

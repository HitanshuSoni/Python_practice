tup1=(32,43,65,67,[54,89],98,76,(65,94,92));
print(tup1[::-1])

for i in reversed(tup1):
    
    print(i)

lst1=list(tup1)
lst1.reverse();
tup1=lst1
tup1=tuple(lst1)
print(tup1)

print(type(reversed(tup1)))


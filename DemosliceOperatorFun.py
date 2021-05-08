import operator 
lst1=[11,22,33,44,55,66]
operator.setitem(lst1,slice(0,3),(65,76,74))
print(lst1)

print(operator.getitem(lst1,slice(3,6)))

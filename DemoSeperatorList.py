list1=['a','b',1,2,21.5,34.65]
intlist=[]
floatlist=[]
stringlist=[]
for value in list1:
    print(value,"->",type(value))
    if isinstance(value,int):
        intlist.append(value)
    elif isinstance(value,float):
        floatlist.append(value)
    else:
        stringlist.append(value)
print(intlist)
print(floatlist)
print(stringlist)
        
    

nestlist=[[12,34],[23,56],[64,87]]
list2=[]
for i,val in enumerate(nestlist):
    for j,val1 in enumerate(nestlist):
        res=(i,j,val1)
        list2.append(res)
print(list2)
    

list1=[[23,56,75],[99,53,55],[23,54,66]]
list2=[]
for i,val in enumerate(list1):
   maxlist=(i+1,max(val))
   list2.append(maxlist)
print(list2)


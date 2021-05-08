list1=[10,2,8,4,5,7,6]
list2=[]
total=0
list2=[(x,y) for x in range(0,len(list1)-1)   for y in list1 if x+y==12]
print(list2)



list3=[]
for i,val in enumerate(list1):
    for j in range(i+1,len(list1)):
        if val+list1[j]==12:
            total=(val,list1[j])
            list3.append(total)


print(list3)

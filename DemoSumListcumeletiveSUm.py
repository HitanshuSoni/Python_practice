list1=[10,20,30,40,50]
list2=[]
total=0
for val in  list1:
    total+=val
    list2.append(total)
    
print(list2)



#sum method
list3=[]
jugad=0
for x in list1:
    
    jugad=sum(list1[0::x])
    list3.append(jugad)

print(list3)
    


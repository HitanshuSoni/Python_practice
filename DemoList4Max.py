mylist=[30,40,50,90]
max1=mylist[0]
for i in range(1,len(mylist)):
    
    print(mylist[i])
    if max1<mylist[i]:
        max1=mylist[i]
print("Max marks is ",max1)

mylist=[30,40,50,90]
status=False
num=int(input("enter number for search"))
for i in range(len(mylist)):
    print(mylist[i])

    if num==mylist[i]:
        status=True
        j=i+1

if status==True:
    print(num,"is found at",j)
else:
    print("Element NOt fOUND")

import sys
lst=[]


ch='y'
while ch=='y':
    val=input("Enter the value")
    #lst=lst+[val]
    
    lst.append(val)
    print("continue::")
    ch=sys.stdin.read(1)
    #ch=input("continue")
    input()

print(lst)
#lst.clear()clear krega
#print(lst)
#del lst puri list uda dega
#print(lst)
del lst[0]# index pe delete krega
print(lst)

import sys
lst=[]


ch='y'
while ch=='y':
    val=input("Enter the value")
    lst=lst+[val]
    print("continue::")
    ch=sys.stdin.read(1)

print(lst)

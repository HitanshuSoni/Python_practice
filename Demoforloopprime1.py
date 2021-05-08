num=int(input("Enter the number"))

status=True
for i in range(2,num//2+1,1):
    if(num%i==0):
        status=False
        break
if(status==True):
    print(num,"is Prime")

else:
    print(num,"is not Prime")

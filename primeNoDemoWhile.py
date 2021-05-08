a=int(input("Enter Number to check Prime or Not"))
i=2
status=True
while(i<=a//2):
    if(a%i==0):
        status=False
        break
    i+=1

if(status==True):
    print(a,"is prime")

else:
    print(a,"is not prime")
        

min1=int(input("Enter the number lower number of range"))
max1=int(input("Enter the number upper number of range"))
count=0
for i in range(min1,max1+1):
    if(i%7==0):
        print(i)
        count+=1
    



print(count)

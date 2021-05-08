min1=int(input("enter any number "))
max1=int(input("enter any number "))
if min1%2==0:
    min1+=1
i=min1;count=0
for k in range (min1,max1+1):
    status = False
    i=i+1
    j=2
    for j in range (j,i//2+1,1):
        
       
        if i%j==0:
            status = True
            break
    if status == False:
        print(i)
        count+=1
print("prime numbers are",count)

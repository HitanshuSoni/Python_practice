min=int(input("enter any number "))
max=int(input("enter any number "))
if min%2==0:
    min+=1
i=min;count=0
while i<=max:
    status = False
    i=i+2
    j=2
    while j<=i/2:
        j+=1
        if i%j==0:
            status = True
            break
    if status == False:
        print(i)
        count+=1
print("prime numbers are",count)

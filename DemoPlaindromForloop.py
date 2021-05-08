min1=int(input("Enter the number of min "))
max1=int(input("Enter the number of max "))
for num in range(min1,max1+1):
    temp=num
    revnum=0
    while temp>0:
        revnum=revnum*10+temp%10
        temp//10
    if num==revnum:
        print(num)

num=int(input("Enter the number tho check it is Angnstrom or not"))
sum2=0
n=num
while(num > 0):
    rem=num%10
    sum2=sum2+(rem*rem*rem)
    num=num//10
if(sum2==num):
    print(n,"is Angrstrom")
else:
    print(n,"not Antstrom")
    

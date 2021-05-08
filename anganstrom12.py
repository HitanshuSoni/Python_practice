import math
num=int(input("Enter the number to get digits"))
sum2=0
n=num
count=0
while(num > 0):
     count+=1
     num=num//10
   
while(num>0):
    sum2=sum2+math.pow(n,count)
    
 

if(sum2==num):
    print(n,"is Angrstrom")
else:
    print(n,"not Antstrom")
    
    

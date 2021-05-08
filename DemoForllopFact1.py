num=int(input("Enter the number for the factorial"))

fact=1
for i in range(num,0,-1):
    fact*=i
    
print(fact)

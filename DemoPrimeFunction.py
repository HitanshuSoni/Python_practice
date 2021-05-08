a=int(input("Enter number"))
def isprime(a):
    
    for i in range(2,a//2+1,1):
        if(a%i==0):
            return False
    else:
            return True
print(isprime(a))
if isprime(a):
    print(a,"is prime")
else:
    print(a,"is not prime")
            
        
         
  


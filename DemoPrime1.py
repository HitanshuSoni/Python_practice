num = int(input("Enter a number: "))
count = 0
i = 2

while(i <= num//2):
    if(num % i == 0):
        count = count + 1
        break
    i = i + 1

if (count == 0 and num != 1):
    print(num,"is a prime")
else:
    print(num," is not a prime")

        

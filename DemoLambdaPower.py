x=int(input("Enter the value"))
y=int(input("Enter the value"))

power=lambda x,y:x**y
print(power(x,y))



def powerF(x,y):
    for y in range(1,y+1):
        power=x**y
    print(power)
powerF(x,y)

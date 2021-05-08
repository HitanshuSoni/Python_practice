import cmath
try:
    a=int(input("Enter the value"))
    b=int(input("Enter the value"))
    c=int(input("Enter the value"))

    minsQuad=lambda a,b,c:(-b-cmath.sqrt(b*b-4*a*c))/(2*a)
    print(minsQuad(a,b,c))

    plusQuad=lambda a,b,c:(-b+cmath.sqrt(b*b-4*a*c))/(2*a)
    print(plusQuad(a,b,c))
except ZeroDivisionError:
    print("Value Of a not be 0")

    

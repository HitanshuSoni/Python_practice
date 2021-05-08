import cmath
list_a=[1,2,3]
list_b=[4,5,6]
list_c=[7,8,9]



print(list(map(lambda a,b,c:-b-cmath.sqrt(b*b-4*a*c)/2*a,list_a,list_b,list_c)))

print(list(map(lambda a,b,c:-b+cmath.sqrt(b*b-4*a*c)/2*a,list_a,list_b,list_c)))



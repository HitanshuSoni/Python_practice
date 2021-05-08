'''try:
    a=10/0
    print(a)
except ArithmeticError:
    print("this statement is raising an exception")
else:
    print("welcome")'''

try:
    a=10/b
    #print(a)
except (ArithmeticError):
    print("ArithmeticError")
except (NameError):
    print("NameError")
else:
    print("welcome")

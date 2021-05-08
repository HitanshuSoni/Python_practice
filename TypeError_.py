
try:
    a=5
    b="string"
    c=a+b
except TypeError:
    print("TypeErroe caught")
else:
    print("No error")

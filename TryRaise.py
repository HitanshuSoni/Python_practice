try:
    a=10
    print(a)
    raise NameError("Hello")
except NameError as e:
    
    print("An Excpetion Occurred")
    print(e)

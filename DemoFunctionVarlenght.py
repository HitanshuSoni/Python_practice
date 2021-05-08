def printinfo(args1,*vartuple):
    print("OutPut is:")
    print(args1)
    for var in vartuple:
        print(var)
    return;
printinfo(10)
printinfo(70,60,50)

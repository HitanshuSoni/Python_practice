def printinfo(args1,*vartuple):
    print("OutPut is:")
    sum1=0
    for var in vartuple:
        sum1+=var
    print(sum1+args1)

    return;

printinfo(7,6,5)

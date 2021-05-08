list1=['a','b',1,2,21.5,34.65]
int1=0
flo=0
stri=0
for value in list1:
    print(value,"->",type(value))
    if isinstance(value,int):#check type
        int1+=1
    elif type(value) == float:
        flo+=1
    else:
        stri+=1
print("Int type",int1)
print("Float type",flo)
print("String type",stri)

    

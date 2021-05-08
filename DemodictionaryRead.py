dict1={}
ch='y'
while(ch=='y' or ch=='Y'):
    
    key=input('Enter  the key  ')
    value=input('Enter the value')
    dict1.update({key:value})
    #dict1[key]=value
    ch=str(input("Do you want to countinue Press y or Y and for print dicitonry print n or N"))
print(dict1)
    

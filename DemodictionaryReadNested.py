dict1={}
ch='y'

while(ch=='y' or ch=='Y'):
    outerkey=input('Enter  the key  ')
       
    dict2={}
    ch1='y'
    
    while(ch1=='y' or ch1=='Y'):
        key=input('Enter  the key  ')
        value=input('Enter the value')
        dict2.update({key:value})
    #dict1[key]=value
        ch1=str(input("Do you want to countinue Press y or Y and for print dicitonry print n or N"))
    dict1.update({outerkey:dict2})
    ch=str(input("Do you want to countinue Press y or Y and for print dicitonry print n or N for go exit from outer side dic "))
    
    
        
    
print(dict1)
    

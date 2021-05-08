tup=(4,5,67,"",(),(45,67),7);
lst=list(tup)
lst2=[]
for val in lst:
    if not((isinstance(val,str) or isinstance(val,tuple) or isinstance(val,list)) and len(val)==0):
        
        lst2.append(val)

    
    

tup1=tuple(lst2)
print(tup1)


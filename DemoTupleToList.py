tup1=(32,43,65,67,[54,89],98,76,(65,94,92));
lst1=list(tup1)
lst2=[]
i=0
for val in lst1:
    
    if isinstance(val,tuple):
        
        lst2=list(val)
        lst2[0]=99
        tup2=tuple(lst2)
        lst1[i]=tup2
    i+=1
tup1=tuple(lst1)
   

print(tup1)

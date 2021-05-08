tup=(4,5,67,"",(),(46,87),[78,54],7);
lst=list(tup)
l=len(lst)
i=0
while(i<l):
   
    if not(lst[i]==int  and len(lst[i])==0):
        i-=1
        l-=1
        lst.remove(lst[i])
    i+=1
    
tup=tuple(lst)    
print(tup)
    

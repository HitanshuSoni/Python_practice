tup=(4,5,67,None,None,7);
lst=list(tup)
l=len(lst)
i=0
while(i<l):
    num=lst[i]
    if lst[i]==None:
        i-=1
        l-=1
        lst.remove(num)
    i+=1
tup=tuple(lst)    

        
        
tup=tuple(lst)        
print(tup)

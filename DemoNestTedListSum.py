lst1=[[1,2,3],[4,5,6],[7,8,9]]
lst2=[]

for val in lst1:
    if isinstance(val,list):
        sum1=0
        for value in val:
            
            sum1+=value
        lst2.append(sum1)
    else:
        lst2.append(val)
print(lst2)
sum2=0
for val1 in lst2:
    
    sum2+=val1
print(sum2)

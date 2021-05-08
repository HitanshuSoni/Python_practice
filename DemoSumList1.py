lst1=[11,12,[1,2,3],[10,15,16,17],20,[22,40,50]]
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

lst1=[[1,2,3],[4,5,6],[7,8,9]]
lst2=[]
sum2=0

for val in lst1:
    if isinstance(val,list):
        sum1=0
        for value in val:
            
            sum1+=value
        lst2.append(sum1)
        sum2+=sum1
print(lst2)
print(sum2)


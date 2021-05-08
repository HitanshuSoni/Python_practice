lst=[10,20,'a',[11,12],['aa','bb','cc']]
for i in range(len(lst)):
    print(lst[i])
for val in lst:
        if isinstance(val,list):
            for value in val:
                print(value)
        else:
            print(val)

   

list1=[('hitu',20),('joker',60),('chandu',5)]
list_b=[]
list_t=[]
list_o=[]

for val in list1:
    
    if val[1]<13:
        list_b.append(val)
    elif val[1] < 20:
        list_t.append(val)
    else:
        list_o.append(val)

print("child",list_b)
print("teenager",list_t)
print("old age",list_o)

def insert1(lst,index,element):
    lst.insert(index,element)
    
    return
    
lst1=[]
insert1(lst1,0,1)
print(lst1)

def append1(lst,element):
    lst.append(element)
    return

append1(lst1,8)
print(lst1)

def del_index(lst,index):
    lst.pop(index)
    return
del_index(lst1,0)
print(lst1)

def del_element(lst,element):
    lst.remove(element)
    return
lst2=[3,5,6,7,6]
del_element(lst2,6)
print(lst2)

def del_all(lst):
    lst.clear()
    return
del_all(lst2)
print(lst2)

lst3=[]
def append_all(list,a,*element):
    list.append(a)
    for ele in element:
        list.append(ele)
    return
    
    
append_all(lst3,2,5,3,5,6,4)
print(lst3)

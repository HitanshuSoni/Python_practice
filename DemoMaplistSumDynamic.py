list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]

print(list(map(lambda *args:sum(args),list1,list2,list3)))

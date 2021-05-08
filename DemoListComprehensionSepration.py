lst=[0,1,0,1,0,1,0,1,0,1,0]
lst1=[num for num in lst if num==0 ]+[num for num in lst if num==1 ]
print(lst1)

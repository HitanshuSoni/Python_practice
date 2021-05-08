lst1=[1,2,3,4,54,65,87,9]
lst2=[43,2,4,5,1,3,65,8]
#lst3=[lst1[i] for i in range(len(lst1)) for j in range(len(lst2)) if lst1[i]==lst2[j]]
lst3=[num for num in lst1  if num in lst2]    

print(lst3)

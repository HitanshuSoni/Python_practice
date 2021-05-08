lst=[2,34,5,7,17,3,6,1,55,44]
lst1=[num for num in lst if num%2==0 ]+[num for num in lst if num%2!=0 ]
print(lst1)

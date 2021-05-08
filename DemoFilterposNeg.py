list1=[12,32,44,56,-21,-12,-56,15,74,0]
posneg=list(filter(lambda x:(x<0),list1))+list(filter(lambda x:(x==0),list1))+list(filter(lambda x:(x>0),list1))
print(posneg)

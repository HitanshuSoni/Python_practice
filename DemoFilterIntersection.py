def interSection(arr1,arr2):
    result=list(filter(lambda x:x in arr1,arr2))
    print("Intersection:",result)

arr1=[1,2,3,4,5,6]
arr2=[1,4,6,78,56,3]
interSection(arr1,arr2)


def notinterSection(arr1,arr2):
    result=list(filter(lambda x:x not in arr1,arr2))
    print("NotIntersection:",result)

arr1=[1,2,3,4,5,6]
arr2=[1,4,6,78,56,3]
notinterSection(arr1,arr2)

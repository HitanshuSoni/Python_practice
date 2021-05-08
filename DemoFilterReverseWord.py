list1=['abab','madam','rar','cdcd']
result=list(filter(lambda x:(x=="".join(reversed(x))),list1))
print(result)

str1=("hello this is bot");
print(str1.split())
EvenList=[]
OddList=[]
for word in str1.split():
    if len(word)%2==0:
        EvenList.append(word)
    else:
        OddList.append(word)
print(EvenList)
print(OddList)
        

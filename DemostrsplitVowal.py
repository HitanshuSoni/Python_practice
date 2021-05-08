str1=("hello this is bot");
print(str1.split())
VowelList=[]

for word in str1.split():
    if (word[0]=='a' or word[0]== 'A'  or word[0]== 'e' or word[0]== 'E' or word[0]== 'i' or word[0]== 'I' or word[0]== 'o' or word[0]== 'O' or word[0]== 'u' or word[0]== 'U'):
        VowelList.append(word)
    
print(VowelList)

        

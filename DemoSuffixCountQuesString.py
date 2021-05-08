dic1={'Hitanshu':'Soni','Shivani':'Soni','Ishan':'Ahmed','Heena':'Chhabra','Alka':'Arora'}
suffix='Soni'
count=0
for val in dic1.values():
    if(val.endswith(suffix)):
        count+=1
        
    
print(count)    

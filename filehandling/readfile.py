fo=open("foo.txt","r+")
print(fo.tell())
str=fo.read(10)
print(fo.tell())
print("Read String is:",str)
fo.seek(0,0) #jump to BOF
print("Afetr seek",fo.tell())
fo.seek(0,2)#jump to eof
print("Afetr seek",fo.tell())
fo.close()
#seek(offset,from where)
#from where =>0,1,2
#0=>BOF
#1=>Current
#2=>Eof

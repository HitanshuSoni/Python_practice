word=input("Enter word for search ")
k=0
with open("foo.txt","r") as f:
	for line in f:
		words=line.split()
		for i in words:
			if(i==words):
				k=k+1
print("Occurence is of word",k,"times")
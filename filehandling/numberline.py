line=open("foo.txt")
cont=line.readlines()
for line1 in cont:
	print(line1.rstrip())
line.close()
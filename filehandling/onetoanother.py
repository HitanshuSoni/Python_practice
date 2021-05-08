with open("foo.txt") as f:
	with open("out.txt" , "w") as outf:
		for line in f:
			outf.write(line)
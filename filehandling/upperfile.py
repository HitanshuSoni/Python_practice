with open("foo.txt") as f:
	with open("outupper.txt" , "w") as outf:
		for line in f:

			outf.write(line.upper())
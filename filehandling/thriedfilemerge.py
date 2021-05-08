with open("foo.txt") as f:
	with open("out.txt") as f2:
		with open("merge.txt" ,"w") as f3:

			for line in f:
				f3.write(line)
			for line in f2:
				f3.write(line)

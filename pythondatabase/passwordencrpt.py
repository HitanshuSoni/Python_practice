import getpass
try:
	p=getpass.getpass()
except Exception as error:
	print("Error",error)
else:
	print("password:",p)

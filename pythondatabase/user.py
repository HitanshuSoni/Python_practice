import sqlite3 as lite
from sqlite3 import Error
import time
import datetime
def sql_connection():
	try:
		con=lite.connect('userpassdb.db')
		print("Connection is established........")
	except Error:
		print(Error)
	finally:
		return con
def sql_table(con):
	cursorObj=con.cursor()
	cursorObj.execute("CREATE TABLE if not exists registerpasstb(username text PRIMARY KEY , password text,dob date, gender text,ques text,ans text,status integer default 0)")
	con.commit()
con=sql_connection()
sql_table(con)
def newUser(con):
	usernm=input("Enter the user name: ")
	passwd=input("Enetr the password: ")
	yy=int(input("Enter Year"))
	mm=int(input("Enter Month"))
	dd=int(input("Enter Date"))
	dob=datetime.date(yy,mm,dd)
	gender=input("Gender: ")
	lst=["your pet name","your favrouit colour","your favrouit food"]
	for i,item in enumerate(lst):
		print("Q",(i+1),item)
	qno=int(input("Choose Question number"))
	ques=lst[qno-1]
	ans=input()
	status=0
	sqlStmt="""insert into registerpasstb (username,password,dob,gender,ques,ans,status) values(?,?,?,?,?,?,?)"""
	cursorObj=con.cursor()
	cursorObj.execute(sqlStmt,(usernm,passwd,dob,gender,ques,ans,status))
	con.commit()
'''def sql_insert(con):
	cursorObj=con.cursor()
	cursorObj.execute("INSERT INTO registerpasstb(username,password,dob,gender)VALUES(?,?,?,?)",entities)
	con.commit()'''
def login(con):
	userlog=input("Enetr Username\n")
	passlog=input("Enetr password\n")
	cursorObj=con.cursor()
	find_user=('SELECT * FROM registerpasstb WHERE username = ? AND password = ? ')
	cursorObj.execute(find_user,[(userlog),(passlog)])
	result=cursorObj.fetchall()
	if result:
		print("Welcome",userlog)
		#qna()
	else:
		print("wrong username or password")
		fpa=input("Press 1 Forgot Password")
		if fpa=='1':
			forgotPassword(con)
		else:
			print("Wrong Choice")


#newUser(con)
def forgotPassword(con):
	usernm=input("Enter user name")
	lst=["your pet name","your favrouit colour","your favrouit food"]
	for i,item in enumerate(lst):
		print("Q",(i+1),item)
	qno=int(input("Choose Question number"))
	ques=lst[qno-1]
	ans=input()
	sqlStmt=('SELECT count(*) from registerpasstb where username=? and ques=? and ans=?' ,(usernm,ques,ans))
	cursorObj=con.cursor()
	#cursorObj.execute(sqlStmt)
	c=cursorObj.fetchall()
	if c:
		newpass=input("Enter new password")
		sqlStmt=('''UPDATE registerpasstb set password=? where username=?''',(newpass,usernm))
login(con)

	
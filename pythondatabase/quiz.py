import sqlite3 as lite
from sqlite3 import Error
import time

def sql_connection():
	try:
		con=lite.connect('userdb.db')
		print("Connection is established........")
	except Error:
		print(Error)
	finally:
		return con
def sql_table(con):
	cursorObj=con.cursor()
	cursorObj.execute("CREATE TABLE if not exists registertb(username text PRIMARY KEY , password text,dob text, gender text)")
	con.commit()
con=sql_connection()
sql_table(con)
def sql_insert(con,entities):
	cursorObj=con.cursor()
	cursorObj.execute("INSERT INTO registertb(username,password,dob,gender)VALUES(?,?,?,?)",entities)
	con.commit()

'''def sql_fetch(con):
	cursorObj=con.cursor()
	cursorObj.execute('SELECT*FROM registertb')

	

	rows=cursorObj.fetchall()
	for row in rows:

		#print(row)
		print("#"*60)
		print("ID=",row[0])
		print("Name=",row[1])
		print("Salary=",row[2])
		print("Deptartment=",row[3])
		print("Position=",row[4])
		print("Hire Date=",row[5])'''
def login(con):
	userlog=input("Enetr Username\n")
	passlog=input("Enetr password\n")
	cursorObj=con.cursor()
	find_user=('SELECT * FROM registertb WHERE username = ? AND password = ? ')
	cursorObj.execute(find_user,[(userlog),(passlog)])
	result=cursorObj.fetchall()
	if result:
		print("Welcome",userlog)
		qna()
	else:
		print("wrong username or password")
	

	

def qna():
	counta=0
	que1="What is capital of India?\n"
	op1a="1.Mumbai\n"
	op1b="2.Delhi\n"
	op1c="3.Bikaner\n"
	op1d="4.Hydrabad\n"
	print(que1,op1a,op1b,op1c,op1d)
	op1ch=input("Enter the choice\n")
	if op1ch=="2":
		counta+=1
	time.sleep(0.4)
	que2="Full form of SQL?\n"
	op2a="1.Strctured Query Language\n"
	op2b="2.Syntax Queue Language\n"
	op2c="3.Script Question Language\n"
	op2d="4.Slow Query Language\n"
	print(que1,op2a,op2b,op2c,op2d)
	op1ch=input("Enter the choice\n")
	if op1ch=="1":
		counta+=1
	time.sleep(0.4)
	per=(counta/2)*100
	print("percent is",per,"%")

'''def  sql_update(con,tup1):
	cursorObj=con.cursor()
	cursorObj.execute('UPDATE registertb SET name=? where rollno=?',tup1)
	con.commit()
'''

if __name__ == '__main__':
	while True:
		time.sleep(0.5)
		print("#"*60)
		time.sleep(0.5)
		ch=input("Enter Your choice..... \nEnter 1 for Put the Information of Participant.\nEnetr 2 for Start Quiz.\nEnter 3 for Exit.\n")

		print("#"*60)
		if ch=="1":
                        usern=input("Enter the username.\n")
                        passw=input("Enter the password\n")
                        dobu=input("Enter the Date of birth\n")
                        gen=input("Gender:\n")
                        
                        entities=(usern,passw,dobu,gen)
                        sql_insert(con,entities)
		
		elif ch=="2":
			#sql_fetch(con)
			
			
			
				login(con)

			

		elif ch=="3":
                        
			exit()
		else:
			print("##############$$$Bad choice$$$#############\n")
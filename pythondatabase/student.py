import sqlite3 as lite
from sqlite3 import Error
import time

def sql_connection():
	try:
		con=lite.connect('studentdb.db')
		print("Connecting.....")
		time.sleep(0.5)
		print("Connection is established........")
	except Error:
		print(Error)
	finally:
		return con
def sql_table(con):
	cursorObj=con.cursor()
	cursorObj.execute("CREATE TABLE if not exists persontb(rollno integer PRIMARY KEY ,name text,age integer,adderess text )")
	con.commit()
con=sql_connection()
sql_table(con)
def sql_insert(con,entities):
	cursorObj=con.cursor()
	cursorObj.execute("INSERT INTO persontb(rollno,name,age,adderess)VALUES(?,?,?,?)",entities)
	con.commit()
def sql_fetch(con):
	cursorObj=con.cursor()
	cursorObj.execute('SELECT*FROM persontb')
	rows=cursorObj.fetchall()
	for row in rows:
		#print(row)
		print("#"*60)
		print("Rollno.=",row[0])
		print("Name=",row[1])
		print("Age=",row[2])
		print("Adderess=",row[3])
def  sql_update(con,tup1):
	cursorObj=con.cursor()
	cursorObj.execute('UPDATE persontb SET name=? where rollno=?',tup1)
	con.commit()
if __name__ == '__main__':
	while True:
		time.sleep(0.5)
		print("#"*60)
		time.sleep(0.5)
		ch=input("Enter Your choice..... \nEnter 1 for Put the Information of Student.\nEnetr 2 for Get the Information.\nEnter 3 for Update.\nEnetr 4 for Exit\n")

		print("#"*60)
		if ch=="1":
                        roll=int(input("Enter the Rollno.\n"))
                        stuname=input("Enter the Student Name\n")
                        stuage=int(input("Enter the age of Student\n"))
                        stuaddress=input("Student adderess\n")
                        
                        entities=(roll,stuname,stuage,stuaddress)
                        sql_insert(con,entities)
		
		elif ch=="2":
			sql_fetch(con)
		elif ch=="3":
			uroll=int(input("Enter the  Rollno.\n"))
			uname=input("Enter the Student Name\n")
			tup1=(uname,uroll)
			sql_update(con,tup1)

		elif ch=="4":
                        
			exit()
		else:
			print("##############$$$Bad choice$$$#############\n")
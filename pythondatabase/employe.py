import sqlite3 as lite
from sqlite3 import Error

def sql_connection():
	try:
		con=lite.connect('company.db')
		print("Connection is established........")
	except Error:
		print(Error)
	finally:
		return con
def sql_table(con):
	cursorObj=con.cursor()
	cursorObj.execute("CREATE TABLE if not exists emp(id integer PRIMARY KEY ,name text,salary real,department text , position text,hireDate text)")
	con.commit()
con=sql_connection()
sql_table(con)
def sql_insert(con,entities):
	cursorObj=con.cursor()
	cursorObj.execute("INSERT INTO emp(id,name,salary,department,position,hireDate)VALUES(?,?,?,?,?,?)",entities)
	con.commit()

def sql_fetch(con):
	cursorObj=con.cursor()
	cursorObj.execute('SELECT*FROM emp')

	

	rows=cursorObj.fetchall()
	for row in rows:

		#print(row)
		print("#"*60)
		print("ID=",row[0])
		print("Name=",row[1])
		print("Salary=",row[2])
		print("Deptartment=",row[3])
		print("Position=",row[4])
		print("Hire Date=",row[5])
		print("#"*60)
	cursorObj.execute('SELECT COUNT (*)FROM emp')

if __name__ == '__main__':
	while True:
		ch=input("Enter Your choice..... \nEnter 1 for Put the Information of user.\nEnetr 2 for Get the Information.\n Enter 3 for Exit.")
		if ch=="1":
                        ide=int(input("Enter the emp id.\n"))
                        namee=input("Enter the Employee Name\n")
                        salarye=float(input("Enter the salary of employee\n"))
                        dept=input("Employee Department\n")
                        positione=input("Employee Position\n")
                        hireDatee=input("Enter hire Date\n")
                        entities=(ide,namee,salarye,dept,positione,hireDatee)
                        sql_insert(con,entities)
                        
		
		elif ch=="2":
			sql_fetch(con)


		elif ch=="3":
                        
			exit()
		else:
			print("Bad choice\n")
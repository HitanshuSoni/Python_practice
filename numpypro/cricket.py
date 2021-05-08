import sqlite3
import matplotlib.pyplot as plt 
con = sqlite3.connect('Cricket.db')
def sql_insertIndia(con,entities):
    cursorObj=con.cursor()
    cursorObj.execute('CREATE TABLE IF NOT EXISTS TeamIndia(Player_name,Speciality)')
    values=[(Player_name,Speciality)]
    cursorObj.executemany('INSERT INTO TeamIndia values(?,?)',values)
    con.commit()
def sql_fetchIndia(con):
    cursorObj=con.cursor()
    cursorObj.execute('SELECT * FROM TeamIndia')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
def sql_insertAus(con,entities):
    cursorObj=con.cursor()
    cursorObj.execute('CREATE TABLE IF NOT EXISTS Aus (Player_name text,Speciality text)')
    values=[(Player_name,Speciality)]
    cursorObj.executemany('INSERT INTO Aus values(?,?)',values)
    con.commit()
def sql_fetchAus(con):
    cursorObj=con.cursor()
    cursorObj.execute('SELECT * FROM Aus')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
def sql_insertstatics(con,entities):
    cursorObj=con.cursor()
    cursorObj.execute('CREATE TABLE IF NOT EXISTS Statics(over,runs,wickets)')
    values=[(over,runs,wickets)]
    cursorObj.executemany('INSERT INTO Statics values(?,?,?)',values)
    con.commit()
def sql_fetchstatics(con):
    cursorObj=con.cursor()
    cursorObj.execute('SELECT * FROM Statics')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    print('\n1. insert ind players\n2. insert aus players\n3. show Indian players \n4. show aus players\n5. insert statics\n6. show statics\n7. exit')
    while True:
        ch1=input("\nEnter Your choice\n")
        if ch1=='1':
            Player_name=input("Enter Player name\n")
            Speciality=input("Enter SPeciality\n")
            entities=(Player_name,Speciality)
            sql_insertIndia(con,entities)
            while True:
                ch2=input("wants to add more\n")
                if ch2=='y':
                    Player_name=input("Enter Player name\n")
                    Speciality=input("Enter SPeciality\n")
                    entities=(Player_name,Speciality)    
                    sql_insertIndia(con,entities)
                elif ch2=='n':
                    break
        elif ch1=='2':
            Player_name=input("Enter Player name\n")
            Speciality=input("Enter SPeciality\n")
            entities=(Player_name,Speciality)
            sql_insertAus(con,entities)
            while True:
                ch3=input("wants to add more\n")
                if ch3=='y':
                    Player_name=input("Enter Player name\n")
                    Speciality=input("Enter SPeciality\n")
                    entities=(Player_name,Speciality)    
                    sql_insertAus(con,entities)
                elif ch3=='n':
                    break
        elif ch1=='3':
            sql_fetchIndia(con)
        elif ch1=='4':
            sql_fetchAus(con)
        elif ch1=='5':
            over=int(input("Enter overs\n"))
            runs=int(input("Enter runs\n"))
            wickets=int(input("Enter wickets\n"))
            entities=(over,runs,wickets)
            sql_insertstatics(con,entities)
            while True:
                ch4=input("wants to add more\n")
                if ch4=='y':
                    over=int(input("Enter overs\n"))
                    runs=int(input("Enter runs\n"))
                    wickets=int(input("Enter wickets\n"))
                    entities=(over,runs,wickets)
                    sql_insertstatics(con,entities)
                elif ch4=='n':
                    break
        elif ch1=='6':
            sql_fetchstatics(con)
        elif ch1=='7':
            exit()
            
                  

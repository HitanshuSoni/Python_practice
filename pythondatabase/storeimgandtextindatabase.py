#blob datatypes
import sqlite3
def convertToBinaryData(filename):
	with open(filename,'rb') as file:
		blobData=file.read()
	return blobData
def insertBLOB(BirdID,name,photoFile,descrFile):
	try:
		con=sqlite3.connect('BirdDatabase.db')
		curs = con.cursor()
		print("Connected to Sqlite")
		curs.execute("""create table if not exists BirdTb(id Integer auto_increment
		primary key,name text,photo blob, descr blob )""")
		sql="""INSERTED INTO BirdTb(id,name,photo,descr) VALUES(?,?,?,?)"""
		birdPhoto=convertToBinaryData(photoFile)
		birdDescr=convertToBinaryData(descrFile)
		curs.execute(sql,BirdID,name,birdPhoto,birdDescr)
		con.commit()
		print("Image and file inserted successfully as a Blob into ")

import mysql.connector
from mysql.connector import errorcode
class Database:
	def __init__(self,user,password,host,port,database):
		self.user = user
		self.password = password
		self.host = host
		self.database = database
		self.port = port
		self.cnx=""
	def Query(self,SQL,SQL_data=None):
		cnx = ""
		cnx = self.DatabaseConnect()
		temp=[]
		if cnx != "":
			cursor = cnx.cursor()
			query = (str(SQL))
			if SQL_data != None:
				cursor.execute(query,SQL_data)
			else:
				cursor.execute(query)
			for i in cursor:
				temp.append(i)
			cnx.close()
			return temp
		else:
			return False
	def SQL_connect_notclose(self):
		self.cnx = ""
		self.cnx = self.DatabaseConnect()
		if self.cnx != "":
			self.cursor = self.cnx.cursor()
		else:
			return False
	def Query_notclose(self,SQL):
		if self.cnx !="":
			cursor = self.cnx.cursor()
			query = str(SQL)
			cursor.execute(query)
			temp=[]
			for i in cursor:
				temp.append(i)
			return temp
		else:
			return False
	def Update(self,SQL,SQL_data=None):
		cnx = ""
		cnx = self.DatabaseConnect()
		temp=[]
		if cnx != "":
			cursor = cnx.cursor()
			query = (str(SQL))
			if SQL_data !=None:cursor.execute(query,SQL_data)
			else:cursor.execute(query)
			cnx.commit()
			cnx.close()
			return True
		else:
			return False
	def close(self):
		self.cnx.close()
	def DatabaseConnect(self):
		try:
			cnx = mysql.connector.connect(user=self.user,password=self.password,host=self.host,port=self.port,database = self.database)
			print("資料庫連接成功")
			return cnx
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				self.log.write ("Something is wrong with your user name or password",1)
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				self.log.write("Database does not exists",1)
			else:
				self.log.write(err,1)

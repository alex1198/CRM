# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python



import mysql.connector

dataBase = mysql.connector.connect(

	host = 'localhost',
	user = 'root',
	passwd = 'Alex@1198'

	)

# prepare a cursor object 
cursorObject = dataBase.cursor()

# create a database 
cursorObject.execute("CREATE DATABASE AlexDB")

print("All Done!!!")

# we can delete this file after making a database connection...
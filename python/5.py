# Py code to connect to MySQL
import mysql.connector 
# Connection string
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
)
# to create cursor object
connection = db.cursor()
# Creates a new DB
connection.execute("create database test_nie_db")
# Lists all the DBs in MySQL
connection.execute("show databases")
for database in connection:
    print(database)
connection = db.cursor()
# Closes the database connection
db.close()



from dotenv import load_dotenv
import os
import ast
import mysql.connector as mc
load_dotenv('.env')

class initializeStudentDB: 

    def createDatabase(self):
        self.dbCursor.execute('CREATE DATABASE student_data')
        print("Database Created Successfully.")

    def useStudentDatabase(self):
        self.dbCursor.execute('USE student_data')
        print("Selected Database Successfully.")

    def createStudentTable(self):
        self.dbCursor.execute(
            '''CREATE TABLE DATA (
                ID int PRIMARY KEY,
                NAME varchar(20),
                AGE int,
                ROLLNO varchar(20),
                BRANCH varchar(50)
            )'''
        )
        print("Table Created Successfully.")
    
    def describeTable(self):
        self.dbCursor.execute('desc DATA')
        indexList = self.dbCursor.fetchall()
        print(indexList)

    def deleteDatabase(self):
        self.dbCursor.execute('drop database student_data')
        print("Database Dropped Successfully.")

    def __init__(self) -> None:
        self.dbConfig = ast.literal_eval(os.environ.get("DBCONFIG"))
        self.db = mc.connect(host=self.dbConfig['host'], user=self.dbConfig['user'], passwd=self.dbConfig['passwd'])
        self.dbCursor = self.db.cursor()
        self.createDatabase()
        self.useStudentDatabase()
        self.createStudentTable()
        self.describeTable()
        # self.deleteDatabase() # uncomment this if you want to drop the database
        self.db.close()
    
db = initializeStudentDB()
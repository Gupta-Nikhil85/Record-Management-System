import mysql.connector as mc
import os
from dotenv import load_dotenv
load_dotenv('.env')

host=os.environ.get("Host")
user=os.environ.get("User")
password=os.environ.get("Password")
table="data"
database="student_data"

def connect_to_database(database):
    mydb = mc.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    return mydb

def add_new_record(id :int, name:str, age:int, roll:str, branch:str) -> dict[str, any]:
    #connecting to database
    db=connect_to_database(database)
    cur=db.cursor()

    #checking if the id exits.
    query="SELECT * FROM " + table + " WHERE id=" + str(id)
    cur.execute(query)
    res=cur.fetchall()

    #if ID entered is unique.
    if len(res) == 0:
        query = "insert into data(id,name,age,rollNo,branch) values(%s,%s,%s,%s,%s)"
        val = (id, name, age, roll, branch)
        cur.execute(query, val)
        db.commit()
        db.close()
        cur.close()
        return {"success":True, "message":"Details Added Successfully"}
    
    db.close()
    cur.close()
    return {"success":False, "message":"Student ID already exist."}


def search_record_by_id(id:int) -> dict[str, any]:
    #connecting to database
    db=connect_to_database(database)
    cur=db.cursor()

    #checking if the id exits.
    query="SELECT * FROM " + table + " WHERE id=" + str(id)
    cur.execute(query)
    res=cur.fetchall()

    #if ID entered is found.
    if len(res) == 0:
        db.close()
        cur.close()
        return {"success":False, "message":"Student ID doesn't exists", "data":None}
    
    db.close()
    cur.close()
    return {"success":True, "message":"Student ID found.", "data":res}

def modify_record(id :int, name:str, age:int, roll:str, branch:str) -> dict[str, any]:
    #connecting to database
    db=connect_to_database(database)
    cur=db.cursor()

    #updating the required record.
    query="UPDATE "+ table+ " SET name=%s, age=%s, rollNo=%s, branch=%s WHERE id="+ str(id)
    val=(name,age,roll,branch)
    cur.execute(query, val)
    db.commit()
    db.close()
    cur.close()
    return {"success":True, "message":"Student Record Updated Successfully."}

def delete_record(id:int) -> dict[str, any]:
    #connecting to database
    db=connect_to_database(database)
    cur=db.cursor()

    #deleting the record.
    query="DELETE FROM "+table+" WHERE id=" + str(id)
    cur.execute(query)
    db.commit()
    db.close()
    cur.close()
    return {"success":True, "message":"Student Deleted Successfully."}

def fetch_all_records() -> dict[str, any]:
    #connecting to database
    db=connect_to_database(database)
    cur=db.cursor()

    #fetching the record.
    query="SELECT * FROM "+table
    cur.execute(query)
    res = cur.fetchall()
    db.close()
    cur.close()
    return {"success":True, "message":"Records Fetched Successfully.", "data":res}

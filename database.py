import pymysql
from tkinter import messagebox

# Global variables
conn = None
mycursor = None

def connect_database():
    global conn, mycursor
    try:
        conn = pymysql.connect(host='localhost', user='root', password='Nisith@2003')
        mycursor = conn.cursor()
    except Exception as e:
        messagebox.showerror('Error', f'Something went wrong: {str(e)}')
        return
    
    # Creating the database
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            Id VARCHAR(50) PRIMARY KEY, 
            Name VARCHAR(30),
            Phone VARCHAR(10),  
            Role VARCHAR(60), 
            Gender VARCHAR(20), 
            Salary DECIMAL(10,2)
        )
    ''')

def insert(id,name,phone,role,gender,salary):
    mycursor.execute('INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))#dynamic data are added
    conn.commit()

#id exist function
def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id=%s',id)
    result=mycursor.fetchone()
    return result[0]>0

def fetch_employee():
    mycursor.execute('SELECT * from data')
    result=mycursor.fetchall()
    return result
# Call the function
connect_database()

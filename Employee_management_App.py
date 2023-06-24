import tkinter as tk
from tkinter import ttk
import pandas as pd
import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin123",
    database = "company_database"
)
conn = db.cursor()
def view_employee():
    conn.execute("select * from employee")
    data = conn.fetchall()
    table = pd.DataFrame(data, columns=['first_name', 'last_name', 'email_id'])
    print(table)
    db.commit()

def add_employee():
    fname = first_name_entry.get()
    lname = last_name_entry.get()
    email = email_id_entry.get()
    conn.execute("""INSERT INTO EMPLOYEE VALUES(%s, %s, %s)""",(fname, lname, email))
    db.commit()
    if(conn):
        print("Data restored")
    else:
        print("error occurred")

def remove_employee():
    fname1 = first_name_entry.get()
    conn.execute("""DELETE FROM employee WHERE first_name=%s""",(fname1,))
    db.commit()

root = tk.Tk()
root.title("Company Database")

mainframe = ttk.Frame(root)
mainframe.grid(column=10, row=0)

ttk.Label(mainframe, text="First Name:").grid(column=0, row=0)
first_name_entry = ttk.Entry(mainframe)
first_name_entry.grid(column=1, row=0)

ttk.Label(mainframe, text="Last Name:").grid(column=0, row=1)
last_name_entry = ttk.Entry(mainframe)
last_name_entry.grid(column=1, row=1)

ttk.Label(mainframe, text="Email ID:").grid(column=0, row=2)
email_id_entry = ttk.Entry(mainframe)
email_id_entry.grid(column=1, row=2)

ttk.Button(mainframe, text="View Employee Table", command=view_employee).grid(column=0, row=3)
ttk.Button(mainframe, text="Add Employee", command=add_employee).grid(column=1,row=3)
ttk.Button(mainframe, text="Remove Employee", command=remove_employee).grid(column=2,row=3)

root.mainloop()

import mysql.connector
from pymysql import*
import xlwt
import pandas.io.sql as sql
import pandas as pd
from tkinter import *
from pandastable import Table, TableModel

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()

class main(Frame):
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400')
        self.main.title('Display')
        self.f = Frame(self.main)
        self.f.pack(fill=BOTH,expand=1)
        self.disp()
    def disp(self):
        

        mycursor.execute("Select * from patient_record")
        r = mycursor.fetchall()
        df = pd.DataFrame(r)
        df.columns = ["Patient Name","Mobile","Patient Id","Address","Age","Gender","Date","Doctor Name","Treatment Given","Additional Remarks"]
        lst = [df.columns.values.tolist()] + df.values.tolist()
        df.to_csv('Records.csv')
        self.table = pt = Table(self.f, dataframe=df,showstatusbar=True)
        pt.show()
        self.back()
    def back(self):
        self.table.close()
#main()

'''self.root = root
        self.root.geometry('500x500')
        self.root.title("Record Page")
        self.view1()
    def view1(self):
        mycursor.execute("Select * from patient_record")
        r = mycursor.fetchall()
        df = pd.DataFrame(r)
        df.columns = ["Patient Name","Mobile","Patient Id","Address","Age","Gender","Date","Doctor Name","Treatment Given","Additional Remarks"]
        lst = [df.columns.values.tolist()] + df.values.tolist()
        total_rows = len(lst)
        total_columns = len(lst[0])
        print(total_rows)
        print(total_columns)
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(self.root, width=10,font=('Arial',16))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
        df.to_csv('Records.csv')'''
        #print(lst)

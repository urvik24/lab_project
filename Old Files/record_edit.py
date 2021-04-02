import mysql.connector
from pymysql import*
import xlwt
import pandas.io.sql as sql
import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import record_main
import record_edit_update
import record_edit_add
import record_edit_delete
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()

def main():
    root=Tk()
    app=upd(root)
class upd():
    def __init__(self,root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Record Page")
        self.page()
    def page(self):
        self.label_0 = Label(self.root, text="Edit Or Delete Existing Record",width = 25,font=("Times New Roman", 20))
        self.label_0.place(x=80,y=10)
        self.b0= Button(self.root, text='Update Record',width=15,command=self.edit).place(x=100,y=80)
        self.b1= Button(self.root, text='Add Details',width=15,command=self.add).place(x=200,y=80)
        self.b2= Button(self.root, text='Delete Record',width=15,command=self.delete).place(x=300,y=80)
        self.b3= Button(self.root, text='Back',width=10,command=self.back).place(x=200,y=400)

    def edit(self):
        record_edit_update.main()
    def add(self):
        record_edit_add.main()
    def delete(self):
        record_edit_delete.main()
    def back(self):
        record_main.main()  
main()

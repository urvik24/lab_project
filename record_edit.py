import mysql.connector
from pymysql import*
import xlwt
import pandas.io.sql as sql
import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

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
        self.label_0 = Label(self.root, text="Edit and Delete",width = 20,font=("Times New Roman", 20))
        self.label_0.place(x=100,y=5)

        '''self.label_10 = Label(self.root, text="EDIT",width = 50,font=("Times New Roman", 10))
        self.label_10.place(x=50,y=80)
        self.label_20 = Label(self.root, text="DELETE",width = 50,font=("Times New Roman", 10))
        self.label_20.place(x=50,y=220)'''

        self.b1= Button(self.root, text='Edit Record',width=15,command=self.edit).place(x=100,y=80)
        self.b2= Button(self.root, text='Delete Record',width=15,command=self.delete).place(x=200,y=80)
        self.b3= Button(self.root, text='Back',width=10,command=self.back).place(x=200,y=400)

    def edit(self):
        print(123)
    def delete(self):
        print(123)
    def back(self):
        print(1234)

#main()

import mysql.connector
from pymysql import*
import xlwt
import pandas.io.sql as sql
import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from pandastable import Table, TableModel
import record_main

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()

def main():
    root=Tk()
    app=record(root)

class record():
    def __init__(self,root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Record Page")
        self.page()
    def page(self):
        self.label_0 = Label(self.root, text="RECORD DISPLAY",width = 20,font=("Times New Roman", 20))
        self.label_0.place(x=100,y=5)

        self.label_0 = Label(self.root, text="TO DISPLAY SELECTED RECORDS",width = 50,font=("Times New Roman", 10))
        self.label_0.place(x=50,y=50)
        self.label_0 = Label(self.root, text="TO DISPLAY ALL RECORDS",width = 50,font=("Times New Roman", 10))
        self.label_0.place(x=50,y=220)
        
        self.label_1 = Label(self.root, text="Search By",width = 20)
        self.label_1.place(x=195,y=80)
        self.cb = IntVar()
        self.Combo = Combobox(self.root,textvariable=self.cb,width=12, values = ('Patient Name','Mobile','Patient Id','Date','Gender'))
        #self.Combo.grid()
        self.Combo['state'] = 'readonly'
        self.Combo.current(0)
        self.Combo.place(x=180,y=100)
        self.entry_search = Entry(self.root)
        self.entry_search.place(x=170,y=130)
        self.b1= Button(self.root, text='Search and Display',width=25,command=self.validate).place(x=150,y=160)

        self.label_2 = Label(self.root, text="Sort By",width = 20)
        self.label_2.place(x=195,y=250)
        self.cb1 = IntVar()
        self.Combo1 = Combobox(self.root,textvariable=self.cb1,width=12, values = ('Patient Name','Patient Id','Gender','Age','Date','Doctor Name'))
        #self.Combo.grid()
        self.Combo1['state'] = 'readonly'
        self.Combo1.current(0)
        self.Combo1.place(x=180,y=270)
        #self.entry_sort = Entry(self.root)
        #self.entry_sort.place(x=170,y=300)
        self.b2= Button(self.root, text='View All Records',width=25,command=self.sort).place(x=150,y=330)

        self.b3= Button(self.root, text='Back',width=5,command=self.back).place(x=200,y=400)
        
    def back(self):
        record_main.main()

    def validate(self):
        search = self.Combo.get()
        if not self.entry_search.get():
                messagebox.showwarning("WARNING","Enter the Details")
        if(search == "Patient Name"):
            y = "patient_name"        
        elif(search == "Mobile"):
            y = "mobile"
        elif(search == "Patient Id"):
            y = "id_number"
        elif(search == "Date"):
            y = "date"  
        elif(search == "Gender"):
            y = "gender"
        q = self.entry_search.get()
        mycursor.execute("SELECT * from patient_record WHERE %s='%s'"%(y,q))
        w = mycursor.fetchall()
        print(type(w))
        if not w:
            messagebox.showerror("ERROR","Entry Doesn't Exist")
            self.entry_search.delete(0,END)
        else:
            print(w)
            

    def search(self):
        '''search = str(self.Combo.get())
        if(search == "Patient Name"):
            y = "patient_name"
        if(search == "Mobile"):
            y = "mobile"
        if(search == "Patient Id"):
            y = "id_number"
        if(search == "Date"):
            y = "date"
        if(search == "Gender"):
            y = "gender"
        x = str(self.entry_search.get())
        mycursor.execute("Select * from patient_record WHERE %s = '%s'"%(y,x))
        fetch = mycursor.fetchall()
        df = pd.DataFrame(fetch)
        print(df)
        self.entry_search.delete(0,END)'''
    def sort(self):
        sort = str(self.Combo1.get())
        if(sort == "Patient Name"):
            i = "patient_name"
        if(sort == "Patient Id"):
            i = "id_number"
        if(sort == "Gender"):
            i = "gender"
        if(sort == "Age"):
            i = "age"
        if(sort == "Date"):
            i = "date"
        if(sort == "Doctor Name"):
            i = "doctor_name"
        mycursor.execute("SELECT * FROM patient_record ORDER BY %s DESC"%(i))
        fetch1 = mycursor.fetchall()
        df = pd.DataFrame(fetch1)
        print(df)

main()

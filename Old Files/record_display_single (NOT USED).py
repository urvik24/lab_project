import mysql.connector
from pymysql import*
import xlwt
import pandas.io.sql as sql
import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import record_display
import record_edit
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()

def main():
    root=Tk()
    app=singledisplay(root)

class singledisplay():
    def __init__(self,root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Record Display")
        self.display()
    def display(self):
        self.label_name = Label(self.root, text="Patient Name",width=20,font=("bold", 10))
        self.label_name.place(x=50,y=60)
        self.label_mobile = Label(self.root, text="Mobile Number",width=20,font=("bold", 10))
        self.label_mobile.place(x=50,y=100)
        self.label_id = Label(self.root, text="Patient Id",width=20,font=("bold", 10))
        self.label_id.place(x=50,y=140)
        self.label_add = Label(self.root, text="Address",width=20,font=("bold", 10))
        self.label_add.place(x=50,y=180)
        self.label_age = Label(self.root, text="Age",width=20,font=("bold", 10))
        self.label_age.place(x=50,y=220)
        self.label_gender = Label(self.root, text="Gender",width=20,font=("bold", 10))
        self.label_gender.place(x=50,y=260)
        self.label_date = Label(self.root, text="Date",width=20,font=("bold", 10))
        self.label_date.place(x=50,y=300)
        self.label_doctor = Label(self.root, text="Referred by ",width=20,font=("bold", 10))
        self.label_doctor.place(x=50,y=340)
        self.label_treatment = Label(self.root, text="Treatment Given",width=20,font=("bold", 10))
        self.label_treatment.place(x=50,y=380)
        self.label_remark = Label(self.root, text="Additional Remarks",width=20,font=("bold", 10))
        self.label_remark.place(x=50,y=420)
        self.b3= Button(self.root, text='Edit',width=10,command=self.editt).place(x=110,y=450)
        self.b4= Button(self.root, text='Back',width=10,command=self.back).place(x=180,y=450)

        y = "patient_name"
        x = "Darsh"
        mycursor.execute("Select * from patient_record WHERE %s = '%s'"%(y,x))
        r = mycursor.fetchone()
        l1 =r[0]
        l2 =r[1]
        l3 =r[2]
        l4 =r[3]
        l5 =r[4]
        l6 =r[5]
        l7 =r[6]
        l8 =r[7]
        l9 =r[8]
        l10 =r[9]
        self.label_1 = Label(self.root, text=l1,width=20,font=("bold", 10))
        self.label_1.place(x=200,y=60)
        self.label_2 = Label(self.root, text=l2,width=20,font=("bold", 10))
        self.label_2.place(x=200,y=100)
        self.label_3 = Label(self.root, text=l3,width=20,font=("bold", 10))
        self.label_3.place(x=200,y=140)
        self.label_4 = Label(self.root, text=l4,width=20,font=("bold", 10))
        self.label_4.place(x=200,y=180)
        self.label_5 = Label(self.root, text=l5,width=20,font=("bold", 10))
        self.label_5.place(x=200,y=220)
        self.label_6 = Label(self.root, text=l6,width=20,font=("bold", 10))
        self.label_6.place(x=200,y=260)
        self.label_7 = Label(self.root, text=l7,width=20,font=("bold", 10))
        self.label_7.place(x=200,y=300)
        self.label_8 = Label(self.root, text=l8,width=20,font=("bold", 10))
        self.label_8.place(x=200,y=340)
        self.label_9 = Label(self.root, text=l9,width=20,font=("bold", 10))
        self.label_9.place(x=200,y=380)
        self.label_10= Label(self.root, text=l10,width=20,font=("bold", 10))
        self.label_10.place(x=200,y=420)


    def back(self):
        record_display.main()
    def editt(self):
        record_edit.main()


main()
        

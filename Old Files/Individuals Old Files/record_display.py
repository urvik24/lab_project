import mysql.connector
from pymysql import*
import xlwt
import pandas.io.sql as sql
import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import record_main
import record_view_patientdetails


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
        self.root.maxsize(500,500)
        self.root.title("Record Page")
        self.page()
    def page(self):
        self.label_0 = Label(self.root, text="RECORD DISPLAY",width = 20,font=("Times New Roman", 20))
        self.label_0.place(x=100,y=5)

        self.label_10 = Label(self.root, text="TO DISPLAY ALL RECORDS IN PARTICULAR ORDER",width = 50,font=("Times New Roman", 10))
        self.label_10.place(x=50,y=80)
        self.label_20 = Label(self.root, text="TO DISPLAY SINGLE RECORD",width = 50,font=("Times New Roman", 10))
        self.label_20.place(x=50,y=220)
        
        self.label_1 = Label(self.root, text="Search By",width = 20)
        self.label_1.place(x=195,y=250)
        self.cb = IntVar()
        self.Combo = Combobox(self.root,textvariable=self.cb,width=12, values = ('Patient Name','Mobile','Patient Id','Date','Gender','Doctor Name'))
        #self.Combo.grid()
        self.Combo['state'] = 'readonly'
        self.Combo.current(0)
        self.Combo.place(x=180,y=270)
        self.entry_search = Entry(self.root)
        self.entry_search.place(x=170,y=300)

        self.label_2 = Label(self.root, text="Sort By",width = 20)
        self.label_2.place(x=200,y=110)
        self.cb1 = IntVar()
        self.Combo1 = Combobox(self.root,textvariable=self.cb1,width=12, values = ('Patient Name','Patient Id','Gender','Age','Date','Doctor Name'))
        #self.Combo1.grid()
        self.Combo1['state'] = 'readonly'
        self.Combo1.current(0)
        self.Combo1.place(x=180,y=130)

        
        self.b1= Button(self.root, text='Search and Display',width=25,command=self.validate).place(x=150,y=330)
        self.b2= Button(self.root, text='View Records',width=20,command=self.sort).place(x=160,y=160)
        self.b3= Button(self.root, text='Back',width=10,command=self.back).place(x=200,y=400)
        self.b4= Button(self.root, text='View All Records',width=20,command=self.all).place(x=170,y=45)

    def all(self):
        record_view.main()
    def back(self):
        record_main.main()
        self.root.destroy

    def validate(self):
        search1 = 123
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
        elif(search == "Doctor Name"):
            y = "doctor_name"
        q = self.entry_search.get()
        mycursor.execute("SELECT * from patient_record WHERE %s='%s'"%(y,q))
        global fetch
        fetch = mycursor.fetchall()
        if not fetch:
            messagebox.showerror("ERROR","Entry Doesn't Exist")
            self.entry_search.delete(0,END)
        else:
            self.xyz1()
            self.entry_search.delete(0,END)            

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
        mycursor.execute("SELECT * FROM patient_record ORDER BY %s"%(i))
        global fetch1
        fetch1 = mycursor.fetchall()
        self.xyz()
    def xyz(self):
        self.newwindow=Toplevel(self.root)
        self.app=window(self.newwindow)
    def xyz1(self):
        self.newwindow1=Toplevel(self.root)
        self.app=window1(self.newwindow1)
class window():
    def __init__(self,root):
        self.root = root
        self.root.geometry('1000x500')
        self.root.maxsize(1100,500)
        self.root.title("Table Display")
        self.sortview()
    def sortview(self):
        tree = Treeview(self.root,height = 20, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10"), show='headings')
        style = Style()
        style.theme_use("clam")
        #style.configure("Treeview",background="white",foreground="black",fieldbackground="silver")
        #style.map("Treeview",background=[('selected','blue')])
        tree.column("#1", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#1", text="Patient Name")
        tree.column("#2", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#2", text="Mobile No")
        tree.column("#3", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#3", text="Patient ID")
        tree.column("#4", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#4", text="Address")
        tree.column("#5", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#5", text="Age")
        tree.column("#6", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#6", text="Gender")
        tree.column("#7", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#7", text="Date")
        tree.column("#8", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#8", text="Doctor Name")
        tree.column("#9", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#9", text="Treatment Given")
        tree.column("#10", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#10", text="Additional Remarks")

        hsb = Scrollbar(self.root, orient="horizontal", command=tree.xview)
        hsb.place(x=0, y=428,width=500)
        tree.configure(xscrollcommand=hsb.set)
        tree.pack()
        s = fetch1
        for x in s:
            tree.insert("", END, values=x)
        self.b1= Button(self.root, text='Quit',width=10,command=self.root.destroy).place(x=500,y=460)

class window1():
    def __init__(self,root):
        self.root = root
        self.root.geometry('1100x500')
        self.root.maxsize(1100,500)
        self.root.title("Table Display")
        self.sortview()
    def sortview(self):
        tree = Treeview(self.root,height = 20, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10"), show='headings')
        style = Style()
        style.theme_use("clam")
        #style.configure("Treeview",background="white",foreground="black",fieldbackground="silver")
        #style.map("Treeview",background=[('selected','blue')])
        tree.column("#1", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#1", text="Patient Name")
        tree.column("#2", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#2", text="Mobile No")
        tree.column("#3", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#3", text="Patient ID")
        tree.column("#4", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#4", text="Address")
        tree.column("#5", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#5", text="Age")
        tree.column("#6", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#6", text="Gender")
        tree.column("#7", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#7", text="Date")
        tree.column("#8", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#8", text="Doctor Name")
        tree.column("#9", anchor=CENTER,minwidth=0, width=100, stretch=YES)
        tree.heading("#9", text="Treatment Given")
        tree.column("#10", anchor=CENTER,minwidth=0, width=100, stretch=YES)
        tree.heading("#10", text="Additional Remarks")

        hsb = Scrollbar(self.root, orient="horizontal", command=tree.xview)
        hsb.place(x=0, y=428,width=500)
        tree.configure(xscrollcommand=hsb.set)
        tree.pack()
        s = fetch
        for x in s:
            tree.insert("", END, values=x)
        self.b2= Button(self.root, text='Quit',width=10,command=self.root.destroy).place(x=500,y=460)

#main()

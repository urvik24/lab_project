import mysql.connector
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
    app=updatedata(root)

class updatedata():
    def __init__(self,root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Update Page")
        self.delete()
    def delete(self):
        self.label_0 = Label(self.root, text="Delete Record",width = 20,font=("Times New Roman", 15))
        self.label_0.place(x=10,y=120)
        self.label_name = Label(self.root, text="Enter Patient Name",width=20,font=("bold", 10))
        self.label_name.place(x=50,y=160)
        self.label_id = Label(self.root, text="Enter Patient ID",width=20,font=("bold", 10))
        self.label_id.place(x=50,y=180)
        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=200,y=160)
        self.entry_2 = Entry(self.root)
        self.entry_2.place(x=200,y=180)
        self.b1= Button(self.root, text='Submit',width=15,command=self.deletevalidate).place(x=150,y=210)
    def deletevalidate(self):
        x = self.entry_1.get()
        y = self.entry_2.get()
        if not self.entry_1.get():
            messagebox.showwarning("WARNING","Enter the Patient's Name")
        if not self.entry_2.get():
            messagebox.showwarning("WARNING","Enter the Patient's ID")
        else:
            mycursor.execute("SELECT patient_name,id_number from patient_record WHERE id_number='%s'"%(y))
            u = mycursor.fetchone()
            print(u)
            if not u:
                messagebox.showwarning("WARNING","Patient Name and ID do not match")
                self.entry_1.delete(0,END)
                self.entry_2.delete(0,END)
            else:
                u1 =str(u[0])
                if(x!=u1):
                    messagebox.showwarning("WARNING","Patient Name and ID do not match")
                    self.entry_1.delete(0,END)
                    self.entry_2.delete(0,END)
                else:
                    self.deletesql()
    def deletesql(self):
        i = self.entry_2.get()
        mycursor.execute("DELETE FROM patient_record WHERE id_number= '%s'" %(i))
        #mycursor.execute("DELETE FROM doctor WHERE patient_id= '%s'" %(i))
        mydb.commit()
        messagebox.showinfo("MESSAGE","Records Deleted Successfully!!")
        self.cleardel()
    def cleardel(self):
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
#main()

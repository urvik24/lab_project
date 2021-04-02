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
        self.edit()
    def edit(self):
        self.label_0 = Label(self.root, text="Update Record",width = 20,font=("Times New Roman", 15))
        self.label_0.place(x=10,y=120)
        self.label_name = Label(self.root, text="Enter Patient Name",width=20,font=("bold", 10))
        self.label_name.place(x=50,y=160)
        self.label_id = Label(self.root, text="Enter Patient ID",width=20,font=("bold", 10))
        self.label_id.place(x=50,y=180)
        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=200,y=160)
        self.entry_2 = Entry(self.root)
        self.entry_2.place(x=200,y=180)
        self.b1= Button(self.root, text='Submit',width=15,command=self.validate).place(x=150,y=210)
        self.b0= Button(self.root, text='Back',width=15,command=self.back).place(x=150,y=430)
    def validate(self):
        x = self.entry_1.get()
        y = self.entry_2.get()
        if not self.entry_1.get():
            messagebox.showwarning("WARNING","Enter the Patient's Name")
        if not self.entry_2.get():
            messagebox.showwarning("WARNING","Enter the Patient's ID")
        else:
            mycursor.execute("SELECT patient_name,id_number from patient_record WHERE id_number='%s'"%(y))
            u = mycursor.fetchone()
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
                    self.update()

    def update(self):
        self.label_0 = Label(self.root, text="Select the Entry you want to Update",width=30,font=("bold", 10))
        self.label_0.place(x=70,y=240)
        self.cb = IntVar()
        self.Combo = Combobox(self.root,textvariable=self.cb,width=12, values = ('mobile','address','age'))
        #self.Combo.grid()
        self.Combo['state'] = 'readonly'
        self.Combo.current(0)
        self.Combo.place(x=150,y=270)
        self.entry_3 = Entry(self.root)
        self.entry_3.place(x=150,y=300)
        self.b2= Button(self.root, text='Submit',width=15,command=self.update1).place(x=150,y=330)
    def update1(self):
        a = self.Combo.get()
        b = self.entry_3.get()
        if not self.entry_3.get():
            messagebox.showwarning("WARNING","Enter the Details")
        if(a == "mobile"):
            if self.entry_3.get().isdigit() == False:
                messagebox.showwarning("WARNING","Enter Only Numerical Values")
                self.entry_3.delete(0,END)
            else:
                if len(str(self.entry_3.get())) > 10:
                    messagebox.showerror("ERROR","Incorrect Mobile Number\nEnter Mobile Number Again")
                    self.entry_3.delete(0,END)
        if(a == "age"):
            if self.entry_3.get().isdigit() == False:
                messagebox.showwarning("WARNING","Enter Only Numerical Values")
                self.entry_3.delete(0,END)
        self.updatesql()
    def updatesql(self):
        a = self.Combo.get()
        b = self.entry_3.get()
        c = self.entry_2.get()
        if not (self.entry_3.get()):
            messagebox.showinfo("ERROR","Enter Details first and then click on Submit Button")  
        else:
            mycursor.execute("UPDATE patient_record SET %s = '%s' WHERE id_number = '%s'" %(a,b,c))
            mydb.commit()
            messagebox.showinfo("MESSAGE","Record Updated Successfully!!")
            self.clear()
    def clear(self):
        self.Combo.current(0)
        self.entry_3.delete(0,END)
    def back(self):
        self.Combo.current(0)
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
        self.entry_3.delete(0,END)
#main()

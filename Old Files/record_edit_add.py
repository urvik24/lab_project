import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import datetime

def main():
    root=Tk()
    app=adddata(root)

class adddata():
    def __init__(self,root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Update Page")
        self.add()
    def add(self):
        self.label_0 = Label(self.root, text="Add Treatment Details",width = 20,font=("Times New Roman", 15))
        self.label_0.place(x=10,y=120)
        self.label_name = Label(self.root, text="Enter Patient Name",width=20,font=("bold", 10))
        self.label_name.place(x=50,y=160)
        self.label_id = Label(self.root, text="Enter Patient ID",width=20,font=("bold", 10))
        self.label_id.place(x=50,y=180)
        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=200,y=160)
        self.entry_2 = Entry(self.root)
        self.entry_2.place(x=200,y=180)
        self.b0= Button(self.root, text='Back',width=15,command=self.back).place(x=150,y=430)
        self.b1= Button(self.root, text='Submit',width=15,command=self.validate).place(x=150,y=210)
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
                    self.adddetail()
    def adddetail(self):
        self.label_date = Label(self.root, text="Date",width=20,font=("bold", 10))
        self.label_date.place(x=50,y=340)
        self.x = datetime.datetime.now().strftime("%d-%m-%Y")

        self.label_date1 = Label(self.root, text=self.x,width=20,font=("bold", 10))
        self.label_date1.place(x=200,y=340)
        
        self.label_doctor = Label(self.root, text="Doctor Name ",width=20,font=("bold", 10))
        self.label_doctor.place(x=50,y=250)
        self.entry_doctor = Entry(self.root)
        self.entry_doctor.place(x=200,y=250)

        self.label_treatment = Label(self.root, text="Treatment Given",width=20,font=("bold", 10))
        self.label_treatment.place(x=50,y=280)
        self.entry_treatment = Entry(self.root,width=40)
        self.entry_treatment.place(x=200,y=280)

        self.label_remark = Label(self.root, text="Additional Remarks",width=20,font=("bold", 10))
        self.label_remark.place(x=50,y=310)
        self.entry_remark = Entry(self.root,width=40)
        self.entry_remark.place(x=200,y=310)
        self.b2= Button(self.root, text='Submit',width=15,command=self.addsql).place(x=150,y=400)
    def addsql(self):
        a = self.entry_1.get()
        b = self.entry_2.get()
        c = self.x
        doctor_name = str(self.entry_doctor.get())
        if(doctor_name == ""):
            doctor_name = "NONE"
        treatment = str(self.entry_treatment.get())
        if(treatment == ""):
            treatment = "NONE"
        remarks = str(self.entry_remark.get())
        if(remarks == ""):
            remarks = "NONE"
        mycursor.execute("insert into doctor(id_number,doctor_name,date,treatment_given,additional_remark)values('%s','%s','%s','%s','%s')" %(b,doctor_name,c,treatment,remarks))
        mydb.commit()
        messagebox.showinfo("MESSAGE","Record Inserted Successfully!!")
        self.cleardata()
    def cleardata(self):
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
        self.entry_doctor.delete(0,END)
        self.entry_treatment.delete(0,END)
        self.entry_remark.delete(0,END)
    def back():
        self.entry_1.delete(0,END)
        self.entry_2.delete(0,END)
        self.entry_doctor.delete(0,END)
        self.entry_treatment.delete(0,END)
        self.entry_remark.delete(0,END)
        
main()

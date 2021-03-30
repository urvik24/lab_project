from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector
from pymysql import*
# import xlwt
import datetime
from datetime import timedelta
# import pandas.io.sql as sql
# import pandas as pd
import record_main
import record_view

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()

def main():
    root=Tk()
    app=record_entry(root)
    

class record_entry():
    def __init__(self,root):
        

        self.root = root
        self.root.geometry('500x550')
        self.root.title("Record entry")
        self.page()

    def page(self):

        self.label_0 = Label(self.root, text="ENTER THE PATIENT DETAILS",font=("Times New Roman", 20))
        self.label_0.place(x=50,y=2)

        self.label_name = Label(self.root, text="Patient Name",width=20,font=("bold", 10))
        self.label_name.place(x=50,y=60)
        self.entry_name = Entry(self.root)
        self.entry_name.place(x=200,y=60)

        self.label_mobile = Label(self.root, text="Mobile Number",width=20,font=("bold", 10))
        self.label_mobile.place(x=50,y=100)

        self.cb = IntVar()
        self.Combo = Combobox(self.root,textvariable=self.cb,width=5, values = ('+91','022','Other'))
        #self.Combo.grid()
        self.Combo['state'] = 'readonly'
        self.Combo.current(0)
        self.Combo.place(x=200,y=100)
        self.entry_mobile = Entry(self.root)
        self.entry_mobile.place(x=250,y=100)

        self.label_id = Label(self.root, text="Patient Id",width=20,font=("bold", 10))
        self.label_id.place(x=50,y=140)
        self.entry_id = Entry(self.root)
        self.entry_id.place(x=200,y=140)
        #n = mycursor.execute("Select * from patient_records")
        #print(n)
        i = 10
        self.label_id = Label(self.root, text="(Last entered ID is %d)"%(i),width=20,font=("bold", 8))
        self.label_id.place(x=200,y=162)

        self.label_add = Label(self.root, text="Address",width=20,font=("bold", 10))
        self.label_add.place(x=50,y=180)
        self.entry_add = Entry(self.root,width=40)
        self.entry_add.place(x=200,y=180)

        self.label_age = Label(self.root, text="Age",width=20,font=("bold", 10))
        self.label_age.place(x=50,y=220)
        self.entry_age = Entry(self.root,width=20)
        self.entry_age.place(x=200,y=220)
        
        self.label_gender = Label(self.root, text="Gender",width=20,font=("bold", 10))
        self.label_gender.place(x=50,y=260)
        self.radio = IntVar()
        self.radio.set(1)
        self.radio_opt = {1 : 'MALE', 2: "FEMALE"}
        '''selection = self.radio.get()
        selection1 = self.radio.get()
        print(selection)
        print(selection1)
        self.R1 = Radiobutton(self.root, text=self.radio_opt[1], variable=self.radio, value=1, command=selection)
        self.R2 = Radiobutton(self.root, text=self.radio_opt[2], variable=self.radio, value=2, command=selection1)
        self.R1.place(x=200,y=260)
        self.R2.place(x=260,y=260)'''

        self.cb1 = IntVar()
        self.Combo1 = Combobox(self.root,textvariable=self.cb1,width=10, values = ('Male','Female'))
        #self.Combo.grid()
        self.Combo1['state'] = 'readonly'
        self.Combo1.current(0)
        self.Combo1.place(x=220,y=260)
        

        self.label_date = Label(self.root, text="Date",width=20,font=("bold", 10))
        self.label_date.place(x=50,y=300)
        self.x = datetime.datetime.now().strftime("%d-%m-%Y")

        self.label_date1 = Label(self.root, text=self.x,width=20,font=("bold", 10))
        self.label_date1.place(x=200,y=300)
        #self.cal = DateEntry(self.root, width=12, background='darkblue',foreground='white', borderwidth=2)
        #self.cal.pack(padx=10, pady=10)
        #self.cal.place(x=200,y=300)

        self.label_doctor = Label(self.root, text="Referred by ",width=20,font=("bold", 10))
        self.label_doctor.place(x=50,y=340)
        self.entry_doctor = Entry(self.root)
        self.entry_doctor.place(x=200,y=340)

        self.label_treatment = Label(self.root, text="Treatment Given",width=20,font=("bold", 10))
        self.label_treatment.place(x=50,y=380)
        self.entry_treatment = Entry(self.root,width=40)
        self.entry_treatment.place(x=200,y=380)

        self.label_remark = Label(self.root, text="Additional Remarks",width=20,font=("bold", 10))
        self.label_remark.place(x=50,y=420)
        self.entry_remark = Entry(self.root,width=40)
        self.entry_remark.place(x=200,y=420)

        self.b1= Button(self.root, text='Submit',width=15,command=self.validate).place(x=170,y=460)
        self.b2= Button(self.root, text='Clear',width=10,command=self.cleardata).place(x=270,y=460)
        self.b3= Button(self.root, text='View Records',width=15,command=self.view).place(x=170,y=500)
        self.b4= Button(self.root, text='Back',width=10,command=self.back).place(x=270,y=500)
   
    def entry(self):
        name = str(self.entry_name.get())
        mobile = str(self.entry_mobile.get())
        id_no = str(self.entry_id.get())
        address = str(self.entry_add.get())
        age = str(self.entry_age.get())
        gender = str(self.Combo1.get())

        '''if(gend == 2):
            print("FEMALE")
            gender = "FEMALE"
        elif(gend == 1):
            print("MALE")
            gender = "MALE"'''
        date = str(self.x)
        print(date)
        doctor_name = str(self.entry_doctor.get())
        if(doctor_name == ""):
            doctor_name = "NONE"
        #multiple doctors
        treatment = str(self.entry_treatment.get())
        if(treatment == ""):
            treatment = "NONE"
        remarks = str(self.entry_remark.get())
        if(remarks == ""):
            remarks = "NONE"

        if not ((self.entry_name.get()) and (self.entry_mobile.get()) and (self.entry_id.get()) and (self.entry_add.get()) and (self.entry_age.get()) ):
            messagebox.showinfo("ERROR","Enter Details first and then click on Submit Button")  
        else:
            #mycursor.execute("insert into doctor(id_number,doctor_name)values('%s','%s')" %(id_no,doctor_name))
            #mycursor.execute("insert into patient_record(patient_name,mobile,id_number,address,age,gender,date,doctor_name,treatment_given,additional_remarks)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(name,mobile,id_no,address,age,gender,date,doctor_name,treatment,remarks))
            #mydb.commit()
            messagebox.showinfo("MESSAGE","Record Inserted Successfully!!")
            resp = messagebox.askquestion("Record Inserted", "Do you want to insert a new Entry?")
            if resp == "yes":
                self.cleardata()
            else:
                self.cleardata()
                self.back()

    def validate(self):
        if not self.entry_name.get():
            messagebox.showwarning("WARNING","Enter the Patient's Name")
        if not self.entry_mobile.get():
            messagebox.showwarning("WARNING","Enter Mobile Number")
        if self.entry_mobile.get():
            if self.entry_mobile.get().isdigit() == False:
                messagebox.showwarning("WARNING","Enter Only Numerical Values in Mobile Number Field")
                self.entry_mobile.delete(0,END)
            else:
                if self.Combo.get() == "+91":
                    if len(str(self.entry_mobile.get())) != 10:
                           messagebox.showerror("ERROR","Incorrect Mobile Number\nEnter Mobile Number Again")
                           self.entry_mobile.delete(0,END)
                if self.Combo.get() == "022":
                    if len(str(self.entry_mobile.get())) != 8:
                            messagebox.showerror("ERROR","Incorrect Landline Number\nEnter Landline Number Again")
                            self.entry_mobile.delete(0,END)
        if not self.entry_id.get():
            messagebox.showinfo("WARNING","Enter the Patient's ID")
        else:
            if self.entry_id.get().isdigit() == False:
                messagebox.showinfo("WARNING","Enter Only Numerical Values in the ID Field")
                self.entry_id.delete(0,END)
            else:
                q = self.entry_id.get()
                mycursor.execute("SELECT id_number from patient_record WHERE id_number='%s'"%(q))
                w = mycursor.fetchone()
                s = str(w)
                t = "("+q+",)"
                if(s==t):
                    messagebox.showerror("ERROR","ID Already Exists")
                    self.entry_id.delete(0,END)
        if not self.entry_add.get():
            messagebox.showwarning("WARNING","Enter the Patient's Address")
        if not self.entry_age.get():
            messagebox.showwarning("WARNING","Enter the Patient's Age")
        else:
            if self.entry_age.get().isdigit() == False:
                messagebox.showerror("ERROR","Enter Only Numerical Values in the Age Field")
                self.entry_age.delete(0,END)
        self.entry()

                          
    def cleardata(self):
        self.entry_name.delete(0,END)
        self.entry_mobile.delete(0,END)
        self.entry_id.delete(0,END)
        self.entry_age.delete(0,END)
        self.entry_add.delete(0,END)
        self.entry_doctor.delete(0,END)
        self.entry_treatment.delete(0,END)
        self.entry_remark.delete(0,END)
        self.radio.set(1)
        #self.x = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        #print(self.x)

    def back(self):
        self.root.deiconify()
        record_main.main()
        
    def view(self):
        record_view.main()
            
#main()

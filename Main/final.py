import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import pandas as pd
import datetime
import record_view_patientdetails
import record_view_medicalrecord
import record_view_selected
from mysql_connector import get_connection

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Gala Lab")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        frameList = [LoginMain, Record, Record_Entry, Record_Edit, Record_Update, Record_Add,Record_Delete, Record_Display]
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.frames = {}
        
        for F in frameList:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginMain)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class LoginMain(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_0 = tk.Label(self, text="LOGIN", font=("Times New Roman", 25), fg='black')
        self.label_id = tk.Label(self, text="Staff ID", width=20, font=("bold", 10))
        self.entry_id = tk.Entry(self)
        self.label_pass = tk.Label(self, text="Password", width=20, font=("bold", 10))
        self.entry_pass = tk.Entry(self, show="*")
        # self.label_5 = tk.Label(self, text="New Account?", width=20, font=("bold", 10))
        self.b = tk.Button(self, text='Submit', width=20, bg='brown', fg='white', command=lambda: self.submit(controller))
        # self.b1 = tk.Button(self, text='Register', width=20, bg='brown', fg='white', command=lambda: controller.show_frame(Register))
        self.loginpage()

    def loginpage(self):
        self.label_0.place(x=200,y=50)
        self.label_id.place(x=80,y=130)
        self.entry_id.place(x=240,y=130)
        self.label_pass.place(x=80,y=180)
        self.entry_pass.place(x=240,y=180)
        # self.label_5.place(x=170,y=290)
        self.b.place(x=180,y=260)
        # self.b1.place(x=180,y=320)

    def submit(self,controller):
        a=str(self.entry_id.get())
        b=str(self.entry_pass.get())
        if(a == ""):
            messagebox.showinfo("MESSAGE","Please Enter ID")
        elif(b == ""):
            messagebox.showinfo("MESSAGE","Please Enter Password")
        else:
            
            mydb = get_connection()
            mycursor = mydb.cursor() 
            mycursor.execute("SELECT login_name from login WHERE login_name='%s'"%(a))
            x = mycursor.fetchone()
            n = str(x)
            m = "('"+a+"',)"
            if(n!=m):
                messagebox.showinfo("MESSAGE","ID Doesn't Exist")
                self.entry_id.delete(0,tk.END)
                self.entry_pass.delete(0,tk.END)
            else:
                mycursor.execute("SELECT password FROM login WHERE login_name= '%s'"%(a))
                for i in mycursor:
                    a1=list(i)
                for i in a1:
                    c=i
                if(b!=c):
                    messagebox.showinfo("MESSAGE","INCORRECT PASSWORD")
                    self.entry_pass.delete(0,tk.END)
                else:
                    self.entry_id.delete(0,tk.END)
                    self.entry_pass.delete(0,tk.END)
                    controller.show_frame(Record)
            
            mydb.close()

'''class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_1 = tk.Label(self, text="Login Details",width=20,font=("Times New Roman", 20))
        self.label_0 = tk.Label(self, text="Enter the details",width=20,font=("Arial", 15))
        self.label_id = tk.Label(self, text="Staff ID",width=20,font=("bold", 10))
        self.entry_id = tk.Entry(self)
        self.label_pass = tk.Label(self, text="Password",width=20,font=("bold", 10))
        self.entry_pass = tk.Entry(self,show="*")
        self.label_conpass = tk.Label(self, text="Confirm Password",width=20,font=("bold", 10))
        self.entry_conpass = tk.Entry(self,show="*")
        self.b1= tk.Button(self, text='Submit',width=10,bg='brown',fg='white',command = lambda: self.newlogin(controller) ).place(x=195,y=275)
        self.b2= tk.Button(self, text='Back',width=10,bg='brown',fg='white', command = lambda: controller.show_frame(LoginMain)).place(x=195,y=315)
        self.newloginpage()

    def newloginpage(self):
        
        self.label_1.place(x=5,y=1)     
        self.label_0.place(x=100,y=60)        
        self.label_id.place(x=68,y=160)
        self.entry_id.place(x=240,y=160)
        self.label_pass.place(x=68,y=200)
        self.entry_pass.place(x=240,y=200)
        self.label_conpass.place(x=68,y=230)
        self.entry_conpass.place(x=240,y=230)


    def newlogin(self,controller):
        staff_id = str(self.entry_id.get())
        password = str(self.entry_pass.get())
        conpass = str(self.entry_conpass.get())

        mydb = get_connection()
        mycursor = mydb.cursor() 
        mycursor.execute("SELECT login_name from login WHERE login_name='%s'"%(staff_id))
        y = mycursor.fetchone()
        i = str(y)
        j = "('"+staff_id+"',)"
        if(i==j):
            messagebox.showinfo("WARNING","ID already exists ")
            self.entry_id.delete(0,tk.END)
            self.entry_pass.delete(0,tk.END)
            self.entry_conpass.delete(0,tk.END)
        else:
            if(password!=conpass):
                messagebox.showinfo("WARNING","Password Doesnt Match ")
                self.entry_pass.delete(0,tk.END)
                self.entry_conpass.delete(0,tk.END)
            else:
                mycursor.execute("insert into login(login_name,password)values('%s','%s')" %(staff_id,password))
                mydb.commit()
                messagebox.showinfo("CREATED","New Login Created")
                self.entry_id.delete(0,tk.END)
                self.entry_pass.delete(0,tk.END)
                self.entry_conpass.delete(0,tk.END)
                controller.show_frame(LoginMain)
        mydb.close()'''
class Record(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.b0= tk.Button(self, text='Log Out',width=10,bg='brown',fg='white',command=lambda: controller.show_frame(LoginMain)).place(x=400,y=20)
        self.b= tk.Button(self, text='Create New Patient Entry',width=21,bg='brown',fg='white',command= lambda: controller.show_frame(Record_Entry)).place(x=180,y=150)
        self.b1= tk.Button(self, text='Edit Existing Patient Record',width=21,bg='brown',fg='white',command=lambda: controller.show_frame(Record_Edit)).place(x=180,y=200)
        self.b2= tk.Button(self, text='View Patient Records',width=21,bg='brown',fg='white',command=lambda: controller.show_frame(Record_Display)).place(x=180,y=250)
        self.b3= tk.Button(self, text='Import to Excel',width=21,bg='brown',fg='white',command=lambda: self.excel()).place(x=180,y=350)
    def excel(self):
        Excel.excel()
        Excel.excel1()
        messagebox.showinfo("Success!!","All Online Data Imported")


    def direction1(self):
        record_view.main()

class Record_Entry(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_0 = tk.Label(self, text="ENTER THE PATIENT DETAILS",font=("Times New Roman", 20))
        self.label_name = tk.Label(self, text="Patient Name  *",width=20,font=("bold", 10),anchor='w',justify='left')
        self.entry_name = tk.Entry(self)
        self.label_mobile = tk.Label(self, text="Mobile Number  *",width=20,font=("bold", 10),anchor='w',justify='left')
        self.entry_mobile = tk.Entry(self)
        self.label_id = tk.Label(self, text="Patient Id  *",width=20,font=("bold", 10),anchor='w',justify='left')
        self.entry_id = tk.Entry(self)
        self.label_add = tk.Label(self, text="Address  *",width=20,font=("bold", 10),anchor='w',justify='left')
        self.entry_add = tk.Entry(self,width=40)
        self.label_age = tk.Label(self, text="Age  *",width=20,font=("bold", 10),anchor='w',justify='left')
        self.entry_age = tk.Entry(self,width=20)
        self.label_gender = tk.Label(self, text="Gender  *",width=20,font=("bold", 10),anchor='w',justify='left')
        self.label_date = tk.Label(self, text="Date",width=20,font=("bold", 10),anchor='w',justify='left')
        self.label_doctor = tk.Label(self, text="Referred by ",width=20,font=("bold", 10),anchor='w',justify='left')
        self.entry_doctor = tk.Entry(self)
        self.label_treatment = tk.Label(self, text="Treatment Given",width=20,font=("bold", 10),anchor='w',justify='left')
        self.entry_treatment = tk.Entry(self,width=40)
        self.label_remark = tk.Label(self, text="Additional Remarks",width=20,font=("bold", 10),anchor='w',justify='left')
        self.entry_remark = tk.Entry(self,width=40)
        self.label_star = tk.Label(self, text="* Compulsory Entries",width=20,font=("bold", 8),anchor='w',foreground='red')
        self.recordEntry(controller)

    def recordEntry(self,controller):
        
        self.label_0.place(x=50,y=2)
        self.label_name.place(x=50,y=60)
        self.entry_name.place(x=200,y=60)
        self.label_mobile.place(x=50,y=100)
        self.entry_mobile.place(x=251,y=100)
        self.label_id.place(x=50,y=140)
        self.entry_id.place(x=200,y=140)
        self.label_add.place(x=50,y=180)
        self.entry_add.place(x=200,y=180)
        self.label_age.place(x=50,y=220)
        self.entry_age.place(x=200,y=220)
        self.label_gender.place(x=50,y=260)
        self.label_doctor.place(x=50,y=340)
        self.entry_doctor.place(x=200,y=340)
        self.label_treatment.place(x=50,y=380)
        self.entry_treatment.place(x=200,y=380)
        self.label_remark.place(x=50,y=420)
        self.entry_remark.place(x=200,y=420)
        self.label_star.place(x=50,y=450)

        self.cb = tk.IntVar()
        self.Combo = ttk.Combobox(self,textvariable=self.cb,width=5, values = ('+91','022','Other'))
        #self.Combo.grid()
        self.Combo['state'] = 'readonly'
        self.Combo.current(0)
        self.Combo.place(x=200,y=100)
               
        self.cb1 = tk.IntVar()
        self.Combo1 = ttk.Combobox(self,textvariable=self.cb1,width=10, values = ('Male','Female'))
        #self.Combo.grid()
        self.Combo1['state'] = 'readonly'
        self.Combo1.current(0)
        self.Combo1.place(x=200,y=260)
        

        self.label_date.place(x=50,y=300)
        self.x = datetime.datetime.now().strftime("%d-%m-%Y")
        self.label_date1 = tk.Label(self, text=self.x,width=20,font=("bold", 10),anchor='w')
        self.label_date1.place(x=200,y=300)
               
        self.b1= tk.Button(self, text='Submit',bg='brown',fg='white',width=15,command=lambda: self.validate(controller)).place(x=170,y=470)
        self.b2= tk.Button(self, text='Clear',bg='brown',fg='white',width=10,command=self.cleardata).place(x=270,y=470)
        # self.b3= tk.Button(self, text='View Records',bg='brown',fg='white',width=15,command=self.view).place(x=170,y=500)
        self.b4= tk.Button(self, text='Back',bg='brown',fg='white',width=10,command=lambda: controller.show_frame(Record)).place(x=230,y=500)

    def validate(self,controller):
        if not self.entry_name.get():
            messagebox.showwarning("WARNING","Enter the Patient's Name")
        if not self.entry_mobile.get():
            messagebox.showwarning("WARNING","Enter Mobile Number")
        if self.entry_mobile.get():
            if self.entry_mobile.get().isdigit() == False:
                messagebox.showwarning("WARNING","Enter Only Numerical Values in Mobile Number Field")
                self.entry_mobile.delete(0,tk.END)
            else:
                if self.Combo.get() == "+91":
                    if len(str(self.entry_mobile.get())) != 10:
                           messagebox.showerror("ERROR","Incorrect Mobile Number\nEnter Mobile Number Again")
                           self.entry_mobile.delete(0,tk.END)
                if self.Combo.get() == "022":
                    if len(str(self.entry_mobile.get())) != 8:
                            messagebox.showerror("ERROR","Incorrect Landline Number\nEnter Landline Number Again")
                            self.entry_mobile.delete(0,tk.END)
        if not self.entry_id.get():
            messagebox.showinfo("WARNING","Enter the Patient's ID")
        else:
            if self.entry_id.get().isdigit() == False:
                messagebox.showwarning("WARNING","Enter Only Numerical Values in the ID Field")
                self.entry_id.delete(0,tk.END)
            else:
                q = self.entry_id.get()
                mydb = get_connection()
                mycursor = mydb.cursor() 
                mycursor.execute("SELECT id_number from patient_record WHERE id_number='%s'"%(q))
                w = mycursor.fetchone()
                mydb.close()
                s = str(w)
                t = "("+q+",)"
                if(s==t):
                    messagebox.showerror("ERROR","ID Already Exists")
                    self.entry_id.delete(0,tk.END)
        if not self.entry_add.get():
            messagebox.showwarning("WARNING","Enter the Patient's Address")
        if not self.entry_age.get():
            messagebox.showwarning("WARNING","Enter the Patient's Age")
        else:
            if self.entry_age.get().isdigit() == False:
                messagebox.showwarning("WARNING","Enter Only Numerical Values in the Age Field")
                self.entry_age.delete(0,tk.END)
        
        self.entry(controller)

    def entry(self,controller):
        name = str(self.entry_name.get())
        mobile = str(self.entry_mobile.get())
        id_no = str(self.entry_id.get())
        address = str(self.entry_add.get())
        age = str(self.entry_age.get())
        gender = str(self.Combo1.get())
        date = str(self.x)
        doctor_name = str(self.entry_doctor.get())
        if(doctor_name == ""):
            doctor_name = "NONE"
        treatment = str(self.entry_treatment.get())
        if(treatment == ""):
            treatment = "NONE"
        remarks = str(self.entry_remark.get())
        if(remarks == ""):
            remarks = "NONE"

        if not ((self.entry_name.get()) and (self.entry_mobile.get()) and (self.entry_id.get()) and (self.entry_add.get()) and (self.entry_age.get()) ):
            messagebox.showinfo("ERROR","Enter Details first and then click on Submit Button")  
        else:

            mydb = get_connection()
            mycursor = mydb.cursor()
            mycursor.execute("insert into doctor(id_number,doctor_name,date,treatment_given,additional_remark)values('%s','%s','%s','%s','%s')" %(id_no,doctor_name,date,treatment,remarks))
            mycursor.execute("insert into patient_record(patient_name,mobile,id_number,address,age,gender)values('%s','%s','%s','%s','%s','%s')" %(name,mobile,id_no,address,age,gender))
            mydb.commit()
            mydb.close()
            messagebox.showinfo("MESSAGE","Record Inserted Successfully!!")
            resp = messagebox.askquestion("Record Inserted", "Do you want to insert a new Entry?")
            Excel.excel()
            Excel.excel1()
            if resp == "yes":
                self.cleardata()
            else:
                self.cleardata()
                self.back(controller)

    def cleardata(self):
        self.entry_name.delete(0,tk.END)
        self.entry_mobile.delete(0,tk.END)
        self.entry_id.delete(0,tk.END)
        self.entry_age.delete(0,tk.END)
        self.entry_add.delete(0,tk.END)
        self.entry_doctor.delete(0,tk.END)
        self.entry_treatment.delete(0,tk.END)
        self.entry_remark.delete(0,tk.END)
    # def view(self):
    #     record_view_patientdetails.main()
    def back(self,controller):
        controller.show_frame(Record)

class Record_Edit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.recordEdit(controller)

    def recordEdit(self,controller):
        self.label_0 = tk.Label(self, text="Modify Existing Record",width = 25,font=("Times New Roman", 20))
        self.label_0.place(x=60,y=30)
        self.b0= tk.Button(self, text='Update Patient Details',width=20,bg='brown',fg='white',command=lambda: controller.show_frame(Record_Update)).place(x=175,y=100)
        self.b1= tk.Button(self, text='Add Medical Record',width=20,bg='brown',fg='white',command=lambda: controller.show_frame(Record_Add)).place(x=175,y=150)
        self.b2= tk.Button(self, text='Delete Record',width=20,bg='brown',fg='white',command=lambda: controller.show_frame(Record_Delete)).place(x=175,y=200)
        self.b3= tk.Button(self, text='Back',width=10,bg='brown',fg='white',command=lambda: controller.show_frame(Record)).place(x=205,y=250)

class Record_Update(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.recordUpdate(controller)

    def recordUpdate(self,controller):
        self.label_0 = tk.Label(self, text="Update Record",width =20,font=("Times New Roman", 20))
        self.label_0.place(x=80,y=80)
        self.label_name = tk.Label(self, text="Enter Patient Name",width=20,font=("bold", 10))
        self.label_name.place(x=80,y=140)
        self.label_id = tk.Label(self, text="Enter Patient ID",width=20,font=("bold", 10))
        self.label_id.place(x=80,y=180)
        self.entry_1 = tk.Entry(self)
        self.entry_1.place(x=240,y=140)
        self.entry_2 = tk.Entry(self)
        self.entry_2.place(x=240,y=180)
    
        self.label_x = tk.Label(self, text="Select the Entry you want to Update",width=30,font=("bold", 10))
        self.label_x.place(x=110,y=250)
        self.cb = tk.IntVar()
        self.Combo = ttk.Combobox(self,textvariable=self.cb,width=12, values = ('mobile','address','age'))
        #self.Combo.grid()
        self.Combo['state'] = 'readonly'
        self.Combo.current(0)
        self.Combo.place(x=195,y=290)
        self.entry_3 = tk.Entry(self)
        self.entry_3.place(x=180,y=320)
        self.b2= tk.Button(self, text='Submit',bg='brown',fg='white',width=15,command=self.update).place(x=180,y=350)
        self.b0= tk.Button(self, text='Back',width=15,bg='brown',fg='white',command=lambda: self.back(controller)).place(x=180,y=430)

    def update(self):
        x = self.entry_1.get()
        y = self.entry_2.get()
        if not self.entry_1.get():
            messagebox.showwarning("WARNING","Enter the Patient's Name")
        if not self.entry_2.get():
            messagebox.showwarning("WARNING","Enter the Patient's ID")
        else:
            mydb = get_connection()
            mycursor = mydb.cursor() 
            mycursor.execute("SELECT patient_name,id_number from patient_record WHERE id_number='%s'"%(y))
            u = mycursor.fetchone()
            mydb.close()
            if not u:
                messagebox.showwarning("WARNING","Patient Name and ID do not match")
                self.entry_1.delete(0,tk.END)
                self.entry_2.delete(0,tk.END)
            else:
                u1 =str(u[0])
                if(x!=u1):
                    messagebox.showwarning("WARNING","Patient Name and ID do not match")
                    self.entry_1.delete(0,tk.END)
                    self.entry_2.delete(0,tk.END)
                    self.entry_3.delete(0,tk.END)
                else:
                    a = self.Combo.get()
                    b = self.entry_3.get()
                    if not self.entry_3.get():
                        messagebox.showwarning("WARNING","Enter the new value")
                    else:
                        if(a == "mobile"):
                            if self.entry_3.get().isdigit() == False:
                                messagebox.showwarning("WARNING","Enter Only Numerical Values")
                                self.entry_3.delete(0,tk.END)
                            else:
                                if len(str(self.entry_3.get())) > 10:
                                    messagebox.showerror("ERROR","Incorrect Mobile Number\nEnter Mobile Number Again")
                                    self.entry_3.delete(0,tk.END)
                        if(a == "age"):
                            if self.entry_3.get().isdigit() == False:
                                messagebox.showwarning("WARNING","Enter Only Numerical Values")
                                self.entry_3.delete(0,tk.END)
                        self.updatesql()
    def updatesql(self):
        a = self.Combo.get()
        b = self.entry_3.get()
        c = self.entry_2.get()
        if not (self.entry_3.get()):
            messagebox.showinfo("ERROR","Enter Details first and then click on Submit Button")  
        else:
            mydb = get_connection()
            mycursor = mydb.cursor() 
            mycursor.execute("UPDATE patient_record SET %s = '%s' WHERE id_number = '%s'" %(a,b,c))
            mydb.commit()
            mydb.close()
            messagebox.showinfo("MESSAGE","Record Updated Successfully!!")
            Excel.excel()
            Excel.excel1()
            self.clear()
    def clear(self):
        self.Combo.current(0)
        self.entry_3.delete(0,tk.END)
    def back(self,controller):
        self.Combo.current(0)
        self.entry_1.delete(0,tk.END)
        self.entry_2.delete(0,tk.END)
        self.entry_3.delete(0,tk.END)
        controller.show_frame(Record_Edit)

class Record_Add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.add(controller)
    def add(self,controller):
        self.label_0 = tk.Label(self, text="Add Medical Details",width =20,font=("Times New Roman", 20))
        self.label_0.place(x=80,y=80)
        self.label_name = tk.Label(self, text="Enter Patient Name",width=20,font=("bold", 10))
        self.label_name.place(x=80,y=150)
        self.label_id = tk.Label(self, text="Enter Patient ID",width=20,font=("bold", 10))
        self.label_id.place(x=80,y=180)
        self.entry_1 = tk.Entry(self)
        self.entry_1.place(x=240,y=150)
        self.entry_2 = tk.Entry(self)
        self.entry_2.place(x=240,y=180)

        self.label_date = tk.Label(self, text="Date",width=20,font=("bold", 10))
        self.label_date.place(x=80,y=220)
        self.x = datetime.datetime.now().strftime("%d-%m-%Y")

        self.label_date1 = tk.Label(self, text=self.x,width=20,font=("bold", 10))
        self.label_date1.place(x=200,y=220)

        self.label_doctor = tk.Label(self, text="Doctor Name ",width=20,font=("bold", 10))
        self.label_doctor.place(x=80,y=250)
        self.entry_doctor = tk.Entry(self)
        self.entry_doctor.place(x=240,y=250)

        self.label_treatment = tk.Label(self, text="Treatment Given",width=20,font=("bold", 10))
        self.label_treatment.place(x=80,y=280)
        self.entry_treatment = tk.Entry(self,width=40)
        self.entry_treatment.place(x=240,y=280)

        self.label_remark = tk.Label(self, text="Additional Remarks",width=20,font=("bold", 10))
        self.label_remark.place(x=80,y=310)
        self.entry_remark = tk.Entry(self,width=40)
        self.entry_remark.place(x=240,y=310)
        self.b2= tk.Button(self, text='Submit',width=15,bg='brown',fg='white',command=self.addsql).place(x=180,y=350)
        self.b0= tk.Button(self, text='Back',width=15,bg='brown',fg='white',command=lambda: self.back(controller)).place(x=180,y=430)
    def addsql(self):
        x = self.entry_1.get()
        y = self.entry_2.get()
        if not self.entry_1.get():
            messagebox.showwarning("WARNING","Enter the Patient's Name")
        if not self.entry_2.get():
            messagebox.showwarning("WARNING","Enter the Patient's ID")
        else:
            mydb = get_connection()
            mycursor = mydb.cursor() 
            mycursor.execute("SELECT patient_name,id_number from patient_record WHERE id_number='%s'"%(y))
            u = mycursor.fetchone()
            if not u:
                messagebox.showwarning("WARNING","Patient Name and ID do not match")
                self.entry_1.delete(0,tk.END)
                self.entry_2.delete(0,tk.END)
            else:
                u1 =str(u[0])
                if(x!=u1):
                    messagebox.showwarning("WARNING","Patient Name and ID do not match")
                    self.entry_1.delete(0,tk.END)
                    self.entry_2.delete(0,tk.END)
                    self.entry_doctor.delete(0,tk.END)
                    self.entry_treatment.delete(0,tk.END)
                    self.entry_remark.delete(0,tk.END)
                else:
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
                    Excel.excel()
                    Excel.excel1()
                    self.cleardata()
                mydb.close()
    def cleardata(self):
        self.entry_1.delete(0,tk.END)
        self.entry_2.delete(0,tk.END)
        self.entry_doctor.delete(0,tk.END)
        self.entry_treatment.delete(0,tk.END)
        self.entry_remark.delete(0,tk.END)
    def back(self,controller):
        self.entry_1.delete(0,tk.END)
        self.entry_2.delete(0,tk.END)
        self.entry_doctor.delete(0,tk.END)
        self.entry_treatment.delete(0,tk.END)
        self.entry_remark.delete(0,tk.END)
        controller.show_frame(Record_Edit)

class Record_Delete(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.delete(controller)
    def delete(self,controller):
        self.label_0 = tk.Label(self, text="Delete Record",width = 20,font=("Times New Roman", 20))
        self.label_0.place(x=80,y=80)
        self.label_name = tk.Label(self, text="Enter Patient Name",width=20,font=("bold", 10))
        self.label_name.place(x=80,y=140)
        self.label_id = tk.Label(self, text="Enter Patient ID",width=20,font=("bold", 10))
        self.label_id.place(x=80,y=180)
        self.entry_1 = tk.Entry(self)
        self.entry_1.place(x=240,y=140)
        self.entry_2 = tk.Entry(self)
        self.entry_2.place(x=240,y=180)
        self.b1= tk.Button(self, text='Submit',width=15,bg='brown',fg='white',command=self.deletevalidate).place(x=180,y=230)
        self.b0= tk.Button(self, text='Back',width=15,bg='brown',fg='white',command=lambda: self.back(controller)).place(x=180,y=430)
    def deletevalidate(self):
        x = self.entry_1.get()
        y = self.entry_2.get()
        if not self.entry_1.get():
            messagebox.showwarning("WARNING","Enter the Patient's Name")
        if not self.entry_2.get():
            messagebox.showwarning("WARNING","Enter the Patient's ID")
        else:
            mydb = get_connection()
            mycursor = mydb.cursor() 
            mycursor.execute("SELECT patient_name,id_number from patient_record WHERE id_number='%s'"%(y))
            u = mycursor.fetchone()
            if not u:
                messagebox.showwarning("WARNING","Patient Name and ID do not match")
                self.entry_1.delete(0,tk.END)
                self.entry_2.delete(0,tk.END)
            else:
                u1 =str(u[0])
                if(x!=u1):
                    messagebox.showwarning("WARNING","Patient Name and ID do not match")
                    self.entry_1.delete(0,tk.END)
                    self.entry_2.delete(0,tk.END)
                else:
                    i = self.entry_2.get()
                    resp = messagebox.askquestion("DELETE!!", "Are You Sure You want to Delete?")
                    if resp == "yes":
                        mycursor.execute("DELETE FROM patient_record WHERE id_number= '%s'" %(i))
                        mycursor.execute("DELETE FROM doctor WHERE id_number= '%s'" %(i))
                        mydb.commit()
                        messagebox.showinfo("MESSAGE","Records Deleted Successfully!!")
                        Excel.excel()
                        Excel.excel1()
                        self.cleardel()
                    else:
                        pass
            mydb.close()
    def cleardel(self):
        self.entry_1.delete(0,tk.END)
        self.entry_2.delete(0,tk.END)
    def back(self,controller):
        self.entry_1.delete(0,tk.END)
        self.entry_2.delete(0,tk.END)
        controller.show_frame(Record_Edit)

class Record_Display(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_0 = tk.Label(self, text="RECORD DISPLAY",width = 20,font=("Times New Roman", 20))
        self.b0= tk.Button(self, text='View Patient Details',bg='brown',fg='white',width=20,command=self.all).place(x=170,y=85)
        self.b1= tk.Button(self, text='View All Medical Records',bg='brown',fg='white',width=20,command=self.all1).place(x=170,y=125)
        self.label_1 = tk.Label(self, text="TO DISPLAY SINGLE RECORD",width = 50,font=("Times New Roman", 10))
        self.label_2 = tk.Label(self, text="Search By",width = 20) 
        self.entry_search = tk.Entry(self)       

        self.recordDisplay(controller)
    
    def recordDisplay(self,controller):
        self.label_0.place(x=100,y=5)
        self.label_1.place(x=50,y=220)
        self.label_2.place(x=160,y=240)
        self.entry_search.place(x=170,y=300)

        self.cb = tk.IntVar()
        self.Combo = ttk.Combobox(self,textvariable=self.cb,width=12, values = ('Patient Name','Mobile','Patient Id','Date','Doctor Name'))
        #self.Combo.grid()
        self.Combo['state'] = 'readonly'
        self.Combo.current(0)
        self.Combo.place(x=190,y=270)
        
        self.b2= tk.Button(self, text='Search and Display',bg='brown',fg='white',width=25,command=lambda: self.validate(controller)).place(x=150,y=330)
        self.b3= tk.Button(self, text='Back',bg='brown',fg='white',width=10,command=lambda:controller.show_frame(Record)).place(x=200,y=400)
        
    def validate(self,controller):
        search = self.Combo.get()
        if not self.entry_search.get():
            messagebox.showwarning("WARNING","Enter the Details")
        if(search == "Patient Name"):
            y = "patient_name"        
        elif(search == "Mobile"):
            y = "mobile"
        elif(search == "Patient Id"):
            y = "doctor.id_number"
        elif(search == "Date"):
            y = "date"  
        elif(search == "Doctor Name"):
            y = "doctor_name"
        q = self.entry_search.get()
        mydb = get_connection()
        mycursor = mydb.cursor() 
        mycursor.execute("""SELECT patient_name,doctor.id_number,date,doctor_name,treatment_given,additional_remark FROM patient_record JOIN doctor ON patient_record.id_number = doctor.id_number WHERE %s = '%s' ORDER BY doctor.id_number """%(y,q))
        self.fetch = mycursor.fetchall()
        mydb = get_connection()
        mycursor = mydb.cursor() 
        if not self.fetch:
            messagebox.showerror("ERROR","Entry Doesn't Exist")
            self.entry_search.delete(0,tk.END)
        else:
            self.Combo.current(0)
            self.entry_search.delete(0,tk.END)
            self.searchDisplay(controller)     
    def all(self):
        record_view_patientdetails.main()
    def all1(self):
        record_view_medicalrecord.main()
    def searchDisplay(self,controller):
        record_view_selected.main(self.fetch)     

class Excel():
    def excel():
        mydb = get_connection()
        mycursor = mydb.cursor() 
        mycursor.execute("""SELECT patient_name,doctor.id_number,date,doctor_name,treatment_given,additional_remark FROM patient_record JOIN doctor ON patient_record.id_number = doctor.id_number ORDER BY doctor.id_number""")
        result = mycursor.fetchall()
        mydb.close()
        df = pd.DataFrame(result)
        df.columns = ["Patient Name","Patient Id","Date","Doctor Name","Treatment Given","Additional Remarks"]
        df.index = df.index + 1
        df.to_csv('Records.csv') 
    def excel1():
        mydb = get_connection()
        mycursor = mydb.cursor() 
        mycursor.execute( "select * from patient_record" )
        result1 = mycursor.fetchall()
        mydb.close()
        df1 = pd.DataFrame(result1)
        df1.columns = ["Patient Name","Mobile","Patient Id","Address","Age","Gender"]
        df1.index = df1.index + 1
        df1.to_csv('Patient Details.csv')   

app = tkinterApp()
app.geometry('500x550')
app.configure(bg='blue')
#app.iconphoto(tk.PhotoImage(file="C:\\Users\\Dharmesh Shah\\Desktop\\lab_project\\Main\\icons.ico"))
app.resizable(0, 0)
app.mainloop()
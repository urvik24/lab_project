from tkinter import *
# import mysql.connector
from tkinter import messagebox, ttk

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()


#Page1
class LoginMain(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)
        self.label_0 = Label(self, text="LOGIN CREDENTIALS", font=("Times New Roman", 20), fg='blue')
        self.label_id = Label(self, text="Staff ID", width=20, font=("bold", 10))
        self.entry_id = Entry(self)
        self.label_pass = Label(self, text="Password", width=20, font=("bold", 10))
        self.entry_pass = Entry(self, show="*")
        self.label_5 = Label(self, text="New Account?", width=20, font=("bold", 10))
        self.b = Button(self, text='Submit', width=20, bg='brown', fg='red', command=self.submit)
        self.b1 = Button(self, text='Register', width=20, bg='brown', fg='red', command=self.open_register)
        self.b2 = Button(self, text='Back', width=10, bg='brown', fg='red', command=self.back)
        self.loginpage()
        
    def loginpage(self):

        # self.label_0.place(x=170, y=50)
        self.label_0.grid(row=0, column=4, padx=10, pady=10)
        self.label_id.grid(row=1, column=4, padx=10, pady=10)
        self.entry_id.grid(row=2, column=4, padx=10, pady=10)
        self.label_pass.grid(row=3, column=4, padx=10, pady=10)
        self.entry_pass.grid(row=4, column=4, padx=10, pady=10)
        self.label_5.grid(row=5, column=4, padx=10, pady=10)
        self.b.grid(row=6, column=4, padx=10, pady=10)
        self.b1.grid(row=7, column=4, padx=10, pady=10)
        self.b2.grid(row=8, column=4, padx=10, pady=10)
        # self.root.mainloop()

    def submit(self):
        a=str(self.entry_id.get())
        b=str(self.entry_pass.get())
        if(a == ""):
            messagebox.showinfo("MESSAGE","Please Enter ID")
        elif(b == ""):
            messagebox.showinfo("MESSAGE","Please Enter Password")
        else:   
            mycursor.execute("SELECT login_name from login WHERE login_name='%s'"%(a))
            x = mycursor.fetchone()
            n = str(x)
            m = "('"+a+"',)"
            if(n!=m):
                messagebox.showinfo("MESSAGE","ID Doesn't Exist")
                self.entry_id.delete(0,END)
                self.entry_pass.delete(0,END)
            else:
                mycursor.execute("SELECT password FROM login WHERE login_name= '%s'"%(a))
                for i in mycursor:
                    a1=list(i)
                for i in a1:
                    c=i
                if(b!=c):
                    messagebox.showinfo("MESSAGE","INCORRECT PASSWORD")
                    self.entry_pass.delete(0,END)
                else:
                    record_main.main()

    def open_register(self, controller):
        pass

    def back(self):
        login.main()

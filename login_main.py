from tkinter import *
import mysql.connector
from tkinter import messagebox
import login
import record_main
import login_register
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()

def main():
    root=Tk()
    app=loginmain(root)

class loginmain():

    def __init__(self,root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Login Page")
        self.loginpage()
        
    def loginpage(self):
        self.label_0 = Label(self.root, text="LOGIN CREDENTIALS",font=("Times New Roman", 20),fg='blue')
        self.label_0.place(x=170,y=50)

        self.label_id = Label(self.root, text="Staff ID",width=20,font=("bold", 10))
        self.label_id.place(x=80,y=130)
        self.entry_id = Entry(self.root)
        self.entry_id.place(x=240,y=130)

        self.label_pass = Label(self.root, text="Password",width=20,font=("bold", 10))
        self.label_pass.place(x=68,y=180)
        self.entry_pass = Entry(self.root,show="*")
        self.entry_pass.place(x=240,y=180)

        self.label_5 = Label(self.root, text="New Account?",width=20,font=("bold", 10))
        self.label_5.place(x=170,y=290)
        
        self.b= Button(self.root, text='Submit',width=20,bg='brown',fg='white',command=self.submit).place(x=180,y=260)
        self.b1= Button(self.root, text='Register',width=20,bg='brown',fg='white',command=self.register).place(x=180,y=320)
        self.b2= Button(self.root, text='Back',width=10,bg='brown',fg='white',command=self.back).place(x=210,y=360)
        
        self.root.mainloop()

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
    def register(self):
        login_register.main()

    def back(self):
        login.main()
        
#main()



                 
                 
                 

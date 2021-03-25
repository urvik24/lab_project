from tkinter import *
import mysql.connector
from tkinter import messagebox
import login_main
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()

def main():
    root=Tk()
    app=newlogin(root)

class newlogin():
    def __init__(self,root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Registration Form")
        self.newloginpage()
    def newloginpage(self):
        self.label_1 = Label(self.root, text="Login Details",width=20,font=("Times New Roman", 20))
        self.label_1.place(x=5,y=1)

        self.label_0 = Label(self.root, text="Enter the details",width=20,font=("Arial", 15))
        self.label_0.place(x=100,y=60)

        self.label_id = Label(self.root, text="Staff ID",width=20,font=("bold", 10))
        self.label_id.place(x=68,y=160)

        self.entry_id = Entry(self.root)
        self.entry_id.place(x=240,y=160)

        self.label_pass = Label(self.root, text="Password",width=20,font=("bold", 10))
        self.label_pass.place(x=68,y=200)
        self.entry_pass = Entry(self.root,show="*")
        self.entry_pass.place(x=240,y=200)
        self.label_conpass = Label(self.root, text="Confirm Password",width=20,font=("bold", 10))
        self.label_conpass.place(x=68,y=230)
        self.entry_conpass = Entry(self.root,show="*")
        self.entry_conpass.place(x=240,y=230)

        self.b1= Button(self.root, text='Submit',width=10,bg='brown',fg='white',command=self.newlogin).place(x=195,y=275)
        self.b2= Button(self.root, text='Back',width=10,bg='brown',fg='white',command=self.back).place(x=195,y=315)
        self.root.mainloop()

    def newlogin(self):
        staff_id = str(self.entry_id.get())
        password = str(self.entry_pass.get())
        conpass = str(self.entry_conpass.get())

        mycursor.execute("SELECT login_name from login WHERE login_name='%s'"%(staff_id))
        y = mycursor.fetchone()
        i = str(y)
        j = "('"+staff_id+"',)"
        if(i==j):
            messagebox.showinfo("WARNING","ID already exists ")
            self.entry_id.delete(0,END)
            self.entry_pass.delete(0,END)
            self.entry_conpass.delete(0,END)
        else:
            if(password!=conpass):
                messagebox.showinfo("WARNING","Password Doesnt Match ")
                self.entry_pass.delete(0,END)
                self.entry_conpass.delete(0,END)
            else:
                mycursor.execute("insert into login(login_name,password)values('%s','%s')" %(staff_id,password))
                mydb.commit()
                messagebox.showinfo("CREATED","New Login Created")
                self.entry_id.delete(0,END)
                self.entry_pass.delete(0,END)
                self.entry_conpass.delete(0,END)
                self.back1()
    def back1(self):
        login_main.main()

    def back(self):
        login_main.main()

#main()

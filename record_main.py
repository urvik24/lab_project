from tkinter import *
import mysql.connector
from tkinter import messagebox
import record_entry
import login_main
import record_view
import record_display

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
        self.root.title("Record Page")
        self.page()
    def page(self):
        self.b0= Button(self.root, text='Log Out',width=10,bg='brown',fg='white',command=self.back).place(x=400,y=20)
        self.b= Button(self.root, text='Create New Record',width=20,bg='brown',fg='white',command=self.direction).place(x=180,y=350)
        self.b1= Button(self.root, text='Edit Existing Record',width=20,bg='brown',fg='white',command=self.direction1).place(x=180,y=400)
        self.b2= Button(self.root, text='View All Records',width=20,bg='brown',fg='white',command=self.direction2).place(x=180,y=450)
        self.root.mainloop()
    def back(self):
        login_main.main()
    def direction(self):
        record_entry.main()
    def direction1(self):
        record_display.main()
    def direction2(self):
        record_view.main()
#doctors
#print krne ka hai
#style

#main()
        

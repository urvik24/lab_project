from tkinter import *
import mysql.connector
from tkinter import messagebox
import login
import record_entry
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
    app=windowmain(root)

class windowmain:
    def __init__(self,root):
        self.root = root
        self.root.geometry('500x500')
        self.root.title("Main Page")

        self.b= Button(self.root, text='Login',width=20,bg='brown',fg='white',command=self.direction).place(x=180,y=350)

        self.b1= Button(self.root, text='View Records',width=20,bg='brown',fg='white',command=self.direction1).place(x=180,y=450)

    def direction(self):
        login.main()
    def direction1(self):
        record_view.main()
#doctors
#print krne ka hai
#style
main()
        

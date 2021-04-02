from tkinter import *
from tkinter import messagebox
import login_main
import record_view_patientdetails

def main():
    root=Tk()
    app=windowmain(root)

class windowmain:
    def __init__(self,root):
        self.root = root
        self.root.geometry('500x500')
        self.b= Button(self.root, text='Login',width=20,bg='brown',fg='white',command=self.login).place(x=180,y=350)      
        self.b1= Button(self.root, text='Records',width=20,bg='brown',fg='white',command=self.login1).place(x=180,y=450)

    def login(self):
        login_main.main()

    def login1(self):
        record_view_patientdetails.main()

#main()

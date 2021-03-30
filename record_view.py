import mysql.connector
import pandas as pd
from tkinter import *
from tkinter.ttk import *
from pandastable import Table, TableModel

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()
def main():
    root=Tk()
    app=Display(root)
class Display():
    def __init__(self,root):
        self.root = root
        self.root.geometry('1100x500')
        self.root.maxsize(1100,500)
        self.root.title("Table Display")
        self.style = Style()
        self.style.theme_use("clam")
        self.display()
    def display(self):
        mycursor.execute("Select * from patient_record")
        r = mycursor.fetchall()
        df = pd.DataFrame(r)
        df.columns = ["Patient Name","Mobile","Patient Id","Address","Age","Gender","Date","Doctor Name","Treatment Given","Additional Remarks"]
        df.to_csv('Records.csv')
        #lst = [df.columns.values.tolist()] + df.values.tolist()
        
        tree = Treeview(self.root,height = 20, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10"), show='headings')
        #style.configure("Treeview",background="white",foreground="black",fieldbackground="silver")
        #style.map("Treeview",background=[('selected','blue')])
        tree.column("#1", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#1", text="Patient Name")
        tree.column("#2", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#2", text="Mobile No")
        tree.column("#3", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#3", text="Patient ID")
        tree.column("#4", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#4", text="Address")
        tree.column("#5", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#5", text="Age")
        tree.column("#6", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#6", text="Gender")
        tree.column("#7", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#7", text="Date")
        tree.column("#8", anchor=CENTER,minwidth=0, width=100, stretch=NO)
        tree.heading("#8", text="Doctor Name")
        tree.column("#9", anchor=CENTER,minwidth=0, width=100, stretch=YES)
        tree.heading("#9", text="Treatment Given")
        tree.column("#10", anchor=CENTER,minwidth=0, width=100, stretch=YES)
        tree.heading("#10", text="Additional Remarks")

        hsb = Scrollbar(self.root, orient="horizontal", command=tree.xview)
        hsb.place(x=0, y=428,width=500)
        tree.configure(xscrollcommand=hsb.set)
        tree.pack()
        for x in r:
            tree.insert("", END, values=x)
        self.b2= Button(self.root, text='Quit',width=10,command=self.root.destroy).place(x=500,y=460)
#main()

'''class main(Frame):
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400')
        self.main.title('Display')
        self.f = Frame(self.main)
        self.f.pack(fill=BOTH,expand=1)
        self.disp()
    def disp(self):
        mycursor.execute("Select * from patient_record")
        r = mycursor.fetchall()
        df = pd.DataFrame(r)
        df.columns = ["Patient Name","Mobile","Patient Id","Address","Age","Gender","Date","Doctor Name","Treatment Given","Additional Remarks"]
        lst = [df.columns.values.tolist()] + df.values.tolist()
        df.to_csv('Records.csv')
        self.table = pt = Table(self.f, dataframe=df,showstatusbar=True)
        pt.show()'''



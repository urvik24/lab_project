from tkinter import *
from tkinter.ttk import *
from mysql_connector import get_connection

def main():
    root=Tk()
    app=Display(root)
class Display():
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x500')
        self.root.maxsize(1100,500)
        self.root.title("Table Display")
        self.style = Style()
        self.style.theme_use("clam")
        self.display()
    def display(self):
        mydb = get_connection()
        mycursor = mydb.cursor() 
        mycursor.execute( "select * from patient_record" )
        result = mycursor.fetchall()
        mydb.close()
        df = pd.DataFrame(result)
        
        tree = Treeview(self.root,height = 20, column=("c1", "c2", "c3","c4","c5","c6"), show='headings')
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

        hsb = Scrollbar(self.root, orient="horizontal", command=tree.xview)
        hsb.place(x=150, y=428,width=500)
        tree.configure(xscrollcommand=hsb.set)
        tree.pack()
        for x in result:
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



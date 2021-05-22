from tkinter import *
from tkinter.ttk import *
from mysql_connector import get_connection
import pandas as pd
import matplotlib.pyplot as plt


def main():
    root=Tk()
    app=Display(root)
class Display():
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x500')
        self.root.maxsize(1100,500)
        self.root.title("Graph")
        self.style = Style()
        self.style.theme_use("clam")
        self.display()
    def display(self):
        mydb = get_connection()
        mycursor = mydb.cursor() 
        mycursor.execute("""SELECT patient_name, treatment.patient_id, date, age, gender, doctor_name, treatment_given, payment
        FROM patient_record JOIN treatment ON patient_record.patient_id = treatment.patient_id ORDER BY treatment.patient_id""") 
        result = mycursor.fetchall()
        mydb.close()
        df = pd.DataFrame(result)
        df.columns = ['Name', 'ID', 'date', 'age', 'gender', 'doctor_name', 'treatment', 'payment']
        #print(df)



        date1 = ["7 April","8 April","9 April","10 April","11 April","12 April","13 April"]
        no = ["10","12","7","12","9","13","6"]
    
        font1 = {'family':'serif','size':30}
        font2 = {'family':'serif','size':15}
        plt.figure(figsize=(16,10))
        plt.grid()

        #plt.plot([row[0] for row in no])
        plt.plot(no,marker='.', markerfacecolor='black', markersize=10)

        plt.xlabel('Date', fontdict = font2)
        plt.ylabel('No of Patients',fontdict = font2)
        plt.title("No of Patients", fontdict = font1)
        #plt.xticks(x, date1)
        #plt.xticks(rotation=90)
        #plt.legend(loc=4, bbox_to_anchor=(1,0), fancybox=True, shadow=True, ncol=2)
        plt.show()

        

        self.b2= Button(self.root, text='Quit',width=10,command=self.root.destroy).place(x=350,y=460)
main()



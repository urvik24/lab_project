import mysql.connector
from pymysql import*
import xlwt
import pandas.io.sql as sql
import pandas as pd

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()

def record_entry():
    name=str(input("Enter Patient's Name: "))
    mobile=int(input("Enter Mobile Number: "))
    #+91/022 10/8 digit
    #if(len(mobile))>10:
     #   print("Enter correct mobile number!")
    id_no=int(input("Enter ID number: "))
    #previous used no
    address=str(input("Enter Address: "))
    age=int(input("Enter Patient's Age: "))
    gender=str(input("Enter Patient's gender: "))
    #Male or Female only(optgven)
    date=str(input("Enter the Date: "))
    #calendar
    doctor_name=str(input("Enter the Doctor's Name: "))
    #multiple doctors
    treatment=str(input("Enter the Treatment Given: "))
    remarks=str(input("Any addictional remarks: "))

    mycursor.execute("insert into patient_record(patient_name,mobile,id_number,address,age,gender,date,treatment_given,additional_remarks)values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(name,mobile,id_no,address,age,gender,date,treatment,remarks))
    mydb.commit()
    mycursor.execute("insert into doctor(doctor_name) values('%s')" %(doctor_name))
    mydb.commit()

    
    #sql = "insert into patient_record(doctor_name) WHERE patient_name = '%s'" %(name)
    #mycursor.execute(sql, doctor_name)
    #mycursor.execute("insert into patient_record(doctor_name) values('%s') WHERE patient_name = ('%s')" %\(doctor_name,name))
    df=sql.read_sql('select * from patient_record',mydb)
    print(df)
    df.to_csv('Records.csv')


record_entry()
    


                    
    

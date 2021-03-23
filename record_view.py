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

def main():
    #df=sql.read_sql('select * from patient_record',mydb)
    #print(df)
    #df.to_csv('Records.csv')
    mycursor.execute("Select * from patient_record")
    r = mycursor.fetchall()
    df = pd.DataFrame(r)
    print(df)
#main()

import mysql as mysql


def get_cursor():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="urvik9293",
        database="lab",
    )
    mycursor=mydb.cursor()
    return mycursor
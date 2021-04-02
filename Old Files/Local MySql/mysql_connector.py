import mysql.connector


def get_connection():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="urvik9293",
        database="lab",
    )
    return mydb
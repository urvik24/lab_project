import mysql.connector


def get_connection():
    mydb=mysql.connector.connect(
        host="nle.obl.mybluehost.me",
        user="nleoblmy_urvik",
        password="urvik9293",
        database="nleoblmy_lab",
    )
    return mydb

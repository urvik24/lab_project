import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()
def login():
    username=str(input("Enter New Username: "))
    password=str(input("Enter Password: "))
    password1=str(input("Re-Enter Password: "))
    if(password == password1):
        print("Password Matched")
        mycursor.execute("insert into login(login_name,password) values('%s','%s')" %(username,password))
        mydb.commit()

        mycursor.execute('select * from login')
        for i in mycursor:
            print(i)
    else:
        print("Password doesnt match, Re-Enter details")
        login()
login()



                 
                 
                 

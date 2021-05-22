from mysql_connector import get_connection
from datetime import datetime
import datetime
mydb = get_connection()
mycursor=mydb.cursor()
'''x = "age"
i = "22"
mycursor.execute("""SELECT patient_name,treatment.patient_id,date,doctor_name,treatment_given,rate
additional_remark FROM patient_record JOIN treatment ON patient_record.patient_id = treatment.patient_id JOIN treatment_name ON
treatment_name.treatment = treatment.treatment_given
WHERE %s = '%s' ORDER BY treatment.patient_id"""%(x,i))
s = mycursor.fetchall()
for i in s:
    print(i)'''
y = "patient_name"
q = "Meet"

mydb = get_connection()
mycursor = mydb.cursor() 
mycursor.execute("""SELECT patient_name,treatment.patient_id,date,doctor_name,treatment_given,rate,additional_remark FROM 
            patient_record JOIN treatment ON patient_record.patient_id = treatment.patient_id JOIN treatment_name ON 
            treatment_name.treatment = treatment.treatment_given WHERE %s = '%s' ORDER BY treatment.patient_id """%(y,q))
fetch = mycursor.fetchall()
mydb.close()
print(fetch)



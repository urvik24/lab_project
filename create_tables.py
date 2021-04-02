import sqlite3


db = sqlite3.connect( "project.db" )
mycursor=db.cursor()
table_login = """CREATE TABLE IF NOT EXISTS`login` (
  `login_name` varchar(20) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`login_name`))"""
table_doctor = """CREATE TABLE IF NOT EXISTS`doctor` (
  `id_number` int(11) NOT NULL,
  `doctor_name` varchar(100) NOT NULL,
  `date` varchar(45) NOT NULL,
  `treatment_given` varchar(45) DEFAULT NULL,
  `additional_remark` varchar(45) DEFAULT NULL)"""
table_record ="""CREATE TABLE IF NOT EXISTS`patient_record` (
  `patient_name` varchar(50) NOT NULL,
  `mobile` bigint(10) NOT NULL,
  `id_number` int(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `age` int(2) NOT NULL,
  `gender` varchar(10) NOT NULL,
  PRIMARY KEY (`patient_name`,`mobile`,`id_number`))"""
#table_record = "DROP TABLE patient_record"
mycursor.execute(table_login)
mycursor.execute(table_doctor)
mycursor.execute(table_record)

db.commit()
db.close()




import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="urvik9293",
    database="lab",
)
mycursor=mydb.cursor()

def Create():
    table_login = """CREATE TABLE `lab`.`login` (`login_name` VARCHAR(20) NOT NULL,`password` VARCHAR(45) NOT NULL,PRIMARY KEY (`login_name`),UNIQUE INDEX `login_name_UNIQUE` (`login_name` ASC) VISIBLE);"""
    table_doctor = """CREATE TABLE `lab`.`doctor`(`doctor_name` VARCHAR(100) NOT NULL,PRIMARY KEY (`doctor_name`));"""
    table_record = """CREATE TABLE `lab`.`patient_record` (`patient_name` VARCHAR(50) NOT NULL,`mobile` BIGINT(10) NOT NULL,`id_number` INT(11) NOT NULL,`address` VARCHAR(100) NOT NULL,`age` INT(3) NOT NULL,`gender` VARCHAR(10) NOT NULL,`date` DATETIME NOT NULL,`treatment_given` VARCHAR(1000) NULL,`additional_remark` VARCHAR(1000) NULL,`doctor_name` VARCHAR(45) NULL,PRIMARY KEY (`patient_name`, `mobile`, `id_number`),UNIQUE INDEX `mobile_UNIQUE` (`mobile` ASC) VISIBLE,UNIQUE INDEX `id_number_UNIQUE` (`id_number` ASC) VISIBLE,INDEX `doctor_name_idx` (`doctor_name` ASC) VISIBLE,CONSTRAINT `doctor_name`FOREIGN KEY (`doctor_name`) REFERENCES `lab`.`doctor` (`doctor_name`) ON DELETE NO ACTION ON UPDATE NO ACTION);"""
    mycursor.execute(table_login)
    mycursor.execute(table_doctor)
    mycursor.execute(table_record)
    mydb.commit()

Create()

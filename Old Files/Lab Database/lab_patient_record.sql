CREATE DATABASE  IF NOT EXISTS `lab` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `lab`;
-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: lab
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `patient_record`
--

DROP TABLE IF EXISTS `patient_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `patient_record` (
  `patient_name` varchar(50) NOT NULL,
  `mobile` bigint(10) NOT NULL,
  `id_number` int(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `age` int(2) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `date` varchar(20) NOT NULL,
  `doctor_name` varchar(45) DEFAULT NULL,
  `treatment_given` varchar(1000) DEFAULT NULL,
  `additional_remarks` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`patient_name`,`mobile`,`id_number`),
  KEY `doctor_name_idx` (`doctor_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_record`
--

LOCK TABLES `patient_record` WRITE;
/*!40000 ALTER TABLE `patient_record` DISABLE KEYS */;
INSERT INTO `patient_record` VALUES ('1',1234567890,2,'2',2,'MALE','3/23/21','00','NONE','NONE'),('1',9819029122,5,'1',12,'MALE','3/23/21','00','NONE','NONE'),('11111',1111111111,0,'00',0,'FEMALE','3/24/21','00','0','0'),('1221',2121212152,203,'303030',20,'Male','28-03-2021 01:07:18','0101','100','100'),('123',1234512345,51,'202',26,'Male','30-03-2021','NONE','NONE','NONE'),('123',9969799290,100,'123',123,'MALE','3/23/21','00','NONE','NONE'),('123333',202020269,669,'65',66,'Male','3/25/21','NONE','NONE','NONE'),('1234',1212454565,48,'121',20,'Male','30-03-2021','20','200','20'),('1234',1245124545,552,'0101',0,'MALE','3/24/21','0101','01','01'),('1234',6598741230,68,'265',20,'Male','31-03-2021','NONE','NONE','NONE'),('123456',2002002002,62,'62',62,'Male','30-03-2021','NONE','NONE','NONE'),('1236',2563563210,565,'565',565,'Male','28-03-2021 01:04:43','656','656','656'),('1254',4545454545,69,'630',30,'Male','31-03-2021','NONE','NONE','NONE'),('15',15,155,'15',15,'Male','3/25/21','15','15','15'),('abcd',1237894560,60,'202',6,'MALE','3/23/21','00','q','q'),('Abhishek',33333,302,'302',20,'Male','30-03-2021','03','03','03'),('Age',101010112,0,'1',1,'MALE','3/25/21','1010','NONE','NONE'),('Bhavya1',1234567890,1234567,'nm',599,'Male','28-03-2021 01:02:49','52','52','52'),('Bjaj',120120122,36,'62',62,'Male','3/25/21','262','262','626'),('bleh',4578961320,65,'566',65,'Male','30-03-2021','NONE','NONE','NONE'),('Darsh',560560564,9000,'303',30,'Male','30-03-2021','NONE','NONE','NONE'),('darsh',1212121256,42,'202',100,'Male','30-03-2021','NONE','00','030'),('Darsh',1234567890,4,'Kandivali',21,'MALE','3/23/21','00','NONE','Good'),('darsh',7878787878,44,'100',1,'Male','30-03-2021','NONE','NONE','NONE'),('Extra',1265437890,46,'202',46,'Female','30-03-2021','NONE','NONE','NONE'),('Fala',6666655555,47,'202',65,'Male','30-03-2021','65','65','65'),('Femi',14141414,1010,'0303',0,'FEMALE','3/9/21','Dr Vikas','Vaccine','Good'),('Femin',0,7,'Mumb',12,'MALE','1/5/21','00','Good','Good'),('ganesh',1414151211,1458,'6548',145,'Male','3/2/21','Dr Gave','NONE','NONE'),('Gaurav',1541455236,585,'198',1000,'Female','3/25/21','1215','NONE','NONE'),('Gauri',1478529369,45555,'012',15,'Female','3/2/21','154','NONE','NONE'),('Hansa',4578457885,9546,'154',1221,'Female','3/25/21','145412','2154','1515'),('Harsh',1414151261,1234,'1234',12,'MALE','3/25/21','NONE','NONE','NONE'),('Hello World',1234561236,1212,'200',20,'Male','30-03-2021','0303','NONE','NONE'),('Hemal',9029852310,15,'202',123,'MALE','3/3/21','00','02','03'),('Ishani',7718801199,2,'Mulund West',20,'MALE','3/12/21','00','Covid','00'),('Ishita',478512693,78,'Mumbai',13,'MALE','3/3/21','00','are','ae'),('Jay',1245789630,19,'Banglore',50,'MALE','3/7/13','00','Fever','GG'),('lolo',1212121212,2000,'20',20,'Male','30-03-2021','NONE','NONE','NONE'),('Parshva',4455667788,6,'qwerty',15,'MALE','3/3/21','00','Cured','!'),('qwertt',303033030,43,'200',20,'Male','30-03-2021','NONE','NONE','NONE'),('Rakesh',4444444444,12,'Jaipur',30,'MALE','3/6/09','00','Covid','Vaccine'),('Shivani',1547803692,25874,'101010',1234,'FEMALE','3/25/21','451','15','12'),('Shivani',9833028428,15,'Dombivli',24,'MALE','3/24/21','00','NONE','NONE'),('Unnati',7208824000,3,'Matunga',22,'MALE','3/2/21','00','Bandage','Recovered'),('Unnu',101010101,89,'16',16,'FEMALE','3/24/21','Dr Urvikkkk','NONE','NONE'),('Urvik',9969799293,1,'Mulund',22,'MALE','3/23/21','00','00','00'),('varsha',1232123123,1452,'Adress',154,'Female','3/25/21','1000','0001','1212'),('Vatsal',12345678,50,'202',20,'MALE','3/24/21','00','NONE','NONE'),('vbvb',202020256,523,'22',0,'Male','30-03-2021','NONE','00','0000'),('Vijaya',1243576890,555,'201',33,'MALE','3/24/21','00','0','0'),('WEshy',1547892360,11111,'123',12,'MALE','3/24/21','Dr signh','1212','1234'),('Yash',9478561230,4323,'aetir',12,'Male','3/4/21','Dr hay','NONE','NONE'),('zxcv',33333,49,'202',25,'Male','30-03-2021','NONE','NONE','NONE');
/*!40000 ALTER TABLE `patient_record` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-31 11:18:24

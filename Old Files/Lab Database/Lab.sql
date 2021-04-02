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
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `doctor` (
  `id_number` int(11) NOT NULL,
  `doctor_name` varchar(100) NOT NULL,
  `date` varchar(45) NOT NULL,
  `treatment_given` varchar(45) DEFAULT NULL,
  `additional_remark` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (1,'Dr V','01-04-2021','Vaccine','Recovery'),(2,'Dr V','01-04-2021','Covid','NONE'),(3,'Dr F','01-04-2021','NONE','NONE'),(4,'Dr V','01-04-2021','Dose','Good'),(2,'Dr F','01-04-2021','Medicine','fever '),(2,'Dr F','01-04-2021','Band Aid','NONE'),(5,'Dr F','01-04-2021','NONE','NONE'),(6,'Dr C','01-04-2021','Meds','Recovered'),(7,'NONE','01-04-2021','NONE','NONE'),(8,'Dr V','01-04-2021','NONE','NONE'),(9,'Dr F','01-04-2021','NONE','NONE'),(8,'Dr H','01-04-2021','NONE','NONE'),(9,'Dr F','01-04-2021','NONE','NONE'),(9,'Dr G','01-04-2021','NONE','NONE'),(7,'Dr M','01-04-2021','NONE','NONE'),(10,'Dr J','01-04-2021','Vaccine','Cured'),(11,'Dr H','01-04-2021','NONE','NONE'),(12,'Dr X','01-04-2021','NONE','NONE'),(13,'NONE','01-04-2021','NONE','NONE'),(15,'Dr F','01-04-2021','NONE','NONE'),(16,'NONE','02-04-2021','NONE','NONE'),(17,'NONE','02-04-2021','NONE','NONE'),(18,'NONE','02-04-2021','NONE','NONE'),(940,'NONE','02-04-2021','NONE','NONE'),(19,'NONE','02-04-2021','NONE','NONE'),(20,'NONE','02-04-2021','NONE','NONE');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `login` (
  `login_name` varchar(20) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`login_name`),
  UNIQUE KEY `login_name_UNIQUE` (`login_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('admin','admin'),('bhavya','bhavya'),('darsh','darsh'),('parshva','parshva'),('root','root'),('urvik','urvik');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

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
  PRIMARY KEY (`patient_name`,`mobile`,`id_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_record`
--

LOCK TABLES `patient_record` WRITE;
/*!40000 ALTER TABLE `patient_record` DISABLE KEYS */;
INSERT INTO `patient_record` VALUES ('Bhavya Karani',9833028428,5,'Dombivli',16,'Male'),('Bina',8079458340,940,'0973453-',90,'Male'),('Darsh',1234567890,4,'Kandivali',21,'Male'),('Dhoni',1234567890,12,'Chennai',38,'Male'),('Femin',7208845632,10,'Dadar',26,'Male'),('Ishani',7718801199,2,'Mulund West',20,'Female'),('Mahek',9769976738,7,'Vashi',15,'Female'),('Malay',7897897890,9,'Navi Mumbai',15,'Male'),('Meet',1234567890,16,'00',0,'Male'),('Parshva',9987200375,6,'Matunga',41,'Male'),('Raina',7897897896,13,'Ranchi',40,'Male'),('Tisha',1004526523,8,'Vashi',30,'Female'),('Unnati',7208824000,3,'Matunga',22,'Female'),('Urvik',9969799293,1,'Mulund',22,'Male'),('Vijay',6544563223,11,'CST',67,'Male'),('Virat',9865788965,15,'Delhi',31,'Male'),('xyz',0,17,'00',0,'Male'),('xyz1',1111111111,18,'200',200,'Male'),('xyz2',1234123422,19,'00',0,'Male'),('xyz3',2222222222,20,'20',20,'Male');
/*!40000 ALTER TABLE `patient_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'lab'
--

--
-- Dumping routines for database 'lab'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-02 20:02:39

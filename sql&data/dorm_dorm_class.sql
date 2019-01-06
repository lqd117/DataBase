-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: dorm
-- ------------------------------------------------------
-- Server version	8.0.13

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
-- Table structure for table `dorm_class`
--

DROP TABLE IF EXISTS `dorm_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `dorm_class` (
  `name` varchar(20) NOT NULL,
  `collegeid_id` varchar(20) DEFAULT NULL,
  `instructorid_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`),
  KEY `dorm_class_collegeid_id_5980d03a_fk_dorm_college_name` (`collegeid_id`),
  KEY `dorm_class_instructorid_id_9a940821_fk_dorm_inst` (`instructorid_id`),
  CONSTRAINT `dorm_class_collegeid_id_5980d03a_fk_dorm_college_name` FOREIGN KEY (`collegeid_id`) REFERENCES `dorm_college` (`name`),
  CONSTRAINT `dorm_class_instructorid_id_9a940821_fk_dorm_inst` FOREIGN KEY (`instructorid_id`) REFERENCES `dorm_instructor` (`user_id_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dorm_class`
--

LOCK TABLES `dorm_class` WRITE;
/*!40000 ALTER TABLE `dorm_class` DISABLE KEYS */;
INSERT INTO `dorm_class` VALUES ('计科-1601','计算机科学与技术',123456),('计科-1602','计算机科学与技术',123456),('计科-1603','计算机科学与技术',123456),('计科-1604','计算机科学与技术',123456),('计科-1605','计算机科学与技术',123456);
/*!40000 ALTER TABLE `dorm_class` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-06 20:38:52

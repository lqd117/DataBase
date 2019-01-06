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
-- Table structure for table `dorm_visitor`
--

DROP TABLE IF EXISTS `dorm_visitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `dorm_visitor` (
  `name` varchar(20) NOT NULL,
  `sex` tinyint(1) NOT NULL,
  `document_type` varchar(20) DEFAULT NULL,
  `documentno` varchar(20) DEFAULT NULL,
  `contact` varchar(200) DEFAULT NULL,
  `dt` datetime(6) NOT NULL,
  `housemasterid_id` int(11) NOT NULL,
  PRIMARY KEY (`name`),
  KEY `dorm_visitor_housemasterid_id_53d2d7de_fk_dorm_hous` (`housemasterid_id`),
  CONSTRAINT `dorm_visitor_housemasterid_id_53d2d7de_fk_dorm_hous` FOREIGN KEY (`housemasterid_id`) REFERENCES `dorm_housemaster` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dorm_visitor`
--

LOCK TABLES `dorm_visitor` WRITE;
/*!40000 ALTER TABLE `dorm_visitor` DISABLE KEYS */;
INSERT INTO `dorm_visitor` VALUES ('1',1,'身份证','111','','2019-01-02 12:38:16.676035',222222),('22',0,'学生证','1033699336722348','1170972087','2019-01-01 15:34:39.725036',222222),('你猜',1,'身份证','1033699336722348','1170972087','2019-01-01 15:34:21.347824',222222);
/*!40000 ALTER TABLE `dorm_visitor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-06 20:38:47

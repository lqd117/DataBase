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
-- Table structure for table `dorm_housemaster`
--

DROP TABLE IF EXISTS `dorm_housemaster`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `dorm_housemaster` (
  `user_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `contact` varchar(200) DEFAULT NULL,
  `buildingid_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `dorm_housemaster_buildingid_id_d6cc08ea_fk_dorm_building_name` (`buildingid_id`),
  CONSTRAINT `dorm_housemaster_buildingid_id_d6cc08ea_fk_dorm_building_name` FOREIGN KEY (`buildingid_id`) REFERENCES `dorm_building` (`name`),
  CONSTRAINT `dorm_housemaster_user_id_e3f3a0e7_fk_dorm_owner_user_id` FOREIGN KEY (`user_id`) REFERENCES `dorm_owner` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dorm_housemaster`
--

LOCK TABLES `dorm_housemaster` WRITE;
/*!40000 ALTER TABLE `dorm_housemaster` DISABLE KEYS */;
INSERT INTO `dorm_housemaster` VALUES (222222,'李二','1170972087','樱花苑1号楼'),(555555,'王五','22222222222222222','樱花苑7号楼');
/*!40000 ALTER TABLE `dorm_housemaster` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-06 20:38:40

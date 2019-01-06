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
-- Table structure for table `dorm_enterapply`
--

DROP TABLE IF EXISTS `dorm_enterapply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `dorm_enterapply` (
  `sno_id` int(11) NOT NULL,
  `dt` datetime(6) NOT NULL,
  `housemaster_check` tinyint(1) DEFAULT NULL,
  `instructor_check` tinyint(1) DEFAULT NULL,
  `secretary_check` tinyint(1) DEFAULT NULL,
  `roomid_id` varchar(20) NOT NULL,
  PRIMARY KEY (`sno_id`),
  UNIQUE KEY `dorm_enterapply_sno_id_roomid_id_dt_8157c409_uniq` (`sno_id`,`roomid_id`,`dt`),
  KEY `dorm_enterapply_roomid_id_434d0192_fk_dorm_room_name` (`roomid_id`),
  CONSTRAINT `dorm_enterapply_roomid_id_434d0192_fk_dorm_room_name` FOREIGN KEY (`roomid_id`) REFERENCES `dorm_room` (`name`),
  CONSTRAINT `dorm_enterapply_sno_id_f2ead7e4_fk_dorm_student_sno_id` FOREIGN KEY (`sno_id`) REFERENCES `dorm_student` (`sno_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dorm_enterapply`
--

LOCK TABLES `dorm_enterapply` WRITE;
/*!40000 ALTER TABLE `dorm_enterapply` DISABLE KEYS */;
INSERT INTO `dorm_enterapply` VALUES (2016014281,'2019-01-03 02:02:47.584943',1,1,NULL,'7-243');
/*!40000 ALTER TABLE `dorm_enterapply` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-06 20:38:41

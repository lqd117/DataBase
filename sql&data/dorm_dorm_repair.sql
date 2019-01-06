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
-- Table structure for table `dorm_repair`
--

DROP TABLE IF EXISTS `dorm_repair`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `dorm_repair` (
  `item` varchar(20) NOT NULL,
  `book_dt` datetime(6) NOT NULL,
  `reason` longtext,
  `fix_dt` datetime(6) DEFAULT NULL,
  `remark` longtext,
  `maintenanceid_id` int(11) DEFAULT NULL,
  `roomid_id` varchar(20) NOT NULL,
  PRIMARY KEY (`item`),
  UNIQUE KEY `dorm_repair_item_roomid_id_book_dt_1bd52dc8_uniq` (`item`,`roomid_id`,`book_dt`),
  KEY `dorm_repair_maintenanceid_id_2822ef90_fk_dorm_main` (`maintenanceid_id`),
  KEY `dorm_repair_roomid_id_9a9aa36a_fk_dorm_room_name` (`roomid_id`),
  CONSTRAINT `dorm_repair_maintenanceid_id_2822ef90_fk_dorm_main` FOREIGN KEY (`maintenanceid_id`) REFERENCES `dorm_maintenance` (`user_id`),
  CONSTRAINT `dorm_repair_roomid_id_9a9aa36a_fk_dorm_room_name` FOREIGN KEY (`roomid_id`) REFERENCES `dorm_room` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dorm_repair`
--

LOCK TABLES `dorm_repair` WRITE;
/*!40000 ALTER TABLE `dorm_repair` DISABLE KEYS */;
INSERT INTO `dorm_repair` VALUES ('1','2019-01-01 09:20:11.999209','1','2019-01-01 14:12:18.145748','修好了',111111,'7-243'),('11','2019-01-01 09:18:51.526247','1','2019-01-01 14:12:42.929470','修好',111111,'7-243'),('111','2019-01-01 09:11:28.016293','11',NULL,NULL,NULL,'7-243'),('33','2019-01-01 09:12:00.098053','33','2019-01-02 11:26:23.039743','修好了',111111,'7-243');
/*!40000 ALTER TABLE `dorm_repair` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-06 20:38:42

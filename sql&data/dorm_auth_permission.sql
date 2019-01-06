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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add owner',1,'add_owner'),(2,'Can change owner',1,'change_owner'),(3,'Can delete owner',1,'delete_owner'),(4,'Can view owner',1,'view_owner'),(5,'Can add log entry',2,'add_logentry'),(6,'Can change log entry',2,'change_logentry'),(7,'Can delete log entry',2,'delete_logentry'),(8,'Can view log entry',2,'view_logentry'),(9,'Can add permission',3,'add_permission'),(10,'Can change permission',3,'change_permission'),(11,'Can delete permission',3,'delete_permission'),(12,'Can view permission',3,'view_permission'),(13,'Can add group',4,'add_group'),(14,'Can change group',4,'change_group'),(15,'Can delete group',4,'delete_group'),(16,'Can view group',4,'view_group'),(17,'Can add user',5,'add_user'),(18,'Can change user',5,'change_user'),(19,'Can delete user',5,'delete_user'),(20,'Can view user',5,'view_user'),(21,'Can add content type',6,'add_contenttype'),(22,'Can change content type',6,'change_contenttype'),(23,'Can delete content type',6,'delete_contenttype'),(24,'Can view content type',6,'view_contenttype'),(25,'Can add session',7,'add_session'),(26,'Can change session',7,'change_session'),(27,'Can delete session',7,'delete_session'),(28,'Can view session',7,'view_session'),(29,'Can add building',8,'add_building'),(30,'Can change building',8,'change_building'),(31,'Can delete building',8,'delete_building'),(32,'Can view building',8,'view_building'),(33,'Can add college',9,'add_college'),(34,'Can change college',9,'change_college'),(35,'Can delete college',9,'delete_college'),(36,'Can view college',9,'view_college'),(37,'Can add class',10,'add_class'),(38,'Can change class',10,'change_class'),(39,'Can delete class',10,'delete_class'),(40,'Can view class',10,'view_class'),(41,'Can add room',11,'add_room'),(42,'Can change room',11,'change_room'),(43,'Can delete room',11,'delete_room'),(44,'Can view room',11,'view_room'),(45,'Can add student',12,'add_student'),(46,'Can change student',12,'change_student'),(47,'Can delete student',12,'delete_student'),(48,'Can view student',12,'view_student'),(49,'Can add instructor',13,'add_instructor'),(50,'Can change instructor',13,'change_instructor'),(51,'Can delete instructor',13,'delete_instructor'),(52,'Can view instructor',13,'view_instructor'),(53,'Can add fee',14,'add_fee'),(54,'Can change fee',14,'change_fee'),(55,'Can delete fee',14,'delete_fee'),(56,'Can view fee',14,'view_fee'),(57,'Can add housemaster',15,'add_housemaster'),(58,'Can change housemaster',15,'change_housemaster'),(59,'Can delete housemaster',15,'delete_housemaster'),(60,'Can view housemaster',15,'view_housemaster'),(61,'Can add mark',16,'add_mark'),(62,'Can change mark',16,'change_mark'),(63,'Can delete mark',16,'delete_mark'),(64,'Can view mark',16,'view_mark'),(65,'Can add secretary',17,'add_secretary'),(66,'Can change secretary',17,'change_secretary'),(67,'Can delete secretary',17,'delete_secretary'),(68,'Can view secretary',17,'view_secretary'),(69,'Can add fee record',18,'add_feerecord'),(70,'Can change fee record',18,'change_feerecord'),(71,'Can delete fee record',18,'delete_feerecord'),(72,'Can view fee record',18,'view_feerecord'),(73,'Can add maintenance',19,'add_maintenance'),(74,'Can change maintenance',19,'change_maintenance'),(75,'Can delete maintenance',19,'delete_maintenance'),(76,'Can view maintenance',19,'view_maintenance'),(77,'Can add repair',20,'add_repair'),(78,'Can change repair',20,'change_repair'),(79,'Can delete repair',20,'delete_repair'),(80,'Can view repair',20,'view_repair'),(81,'Can add enter apply',21,'add_enterapply'),(82,'Can change enter apply',21,'change_enterapply'),(83,'Can delete enter apply',21,'delete_enterapply'),(84,'Can view enter apply',21,'view_enterapply'),(85,'Can add quit apply',22,'add_quitapply'),(86,'Can change quit apply',22,'change_quitapply'),(87,'Can delete quit apply',22,'delete_quitapply'),(88,'Can view quit apply',22,'view_quitapply'),(89,'Can add live record',23,'add_liverecord'),(90,'Can change live record',23,'change_liverecord'),(91,'Can delete live record',23,'delete_liverecord'),(92,'Can view live record',23,'view_liverecord'),(93,'Can add visitor',24,'add_visitor'),(94,'Can change visitor',24,'change_visitor'),(95,'Can delete visitor',24,'delete_visitor'),(96,'Can view visitor',24,'view_visitor');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-06 20:38:36

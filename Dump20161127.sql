-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: localhost    Database: bookaband
-- ------------------------------------------------------
-- Server version	5.7.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `polls_bands`
--

DROP TABLE IF EXISTS `polls_bands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_bands` (
  `b_id` int(11) NOT NULL AUTO_INCREMENT,
  `b_name` varchar(255) NOT NULL,
  `b_email` varchar(255) NOT NULL,
  `b_phone` varchar(31) NOT NULL,
  `b_availability` varchar(255) NOT NULL,
  `b_avgrating` decimal(4,3) DEFAULT NULL,
  `b_price` decimal(10,2) NOT NULL,
  `b_bio` longtext NOT NULL,
  `b_lat` decimal(10,8) NOT NULL,
  `b_lon` decimal(11,8) NOT NULL,
  PRIMARY KEY (`b_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_bands`
--

LOCK TABLES `polls_bands` WRITE;
/*!40000 ALTER TABLE `polls_bands` DISABLE KEYS */;
INSERT INTO `polls_bands` VALUES (1,'The Beatles','ngb2zf@virginia.edu','131-991-8778','Usually available for call on Tuesdays 10 to 4',4.400,199.99,'we are a great band',38.04008230,-78.51999340),(2,'Queen','rjd9se@virginia.edu','798-129-2309','Call from 9 to 5 Monday through Friday',3.700,29.99,'listen to us',38.04008230,-78.51999340),(4,'Pink Floyd','jwz2kn@virginia.edu','632-465-9071','Call from 10 to 3 Tuesday through Thursday',3.100,100.00,'we are the best rock band',38.04008230,-78.51999340);
/*!40000 ALTER TABLE `polls_bands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_events`
--

DROP TABLE IF EXISTS `polls_events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_events` (
  `e_id` int(11) NOT NULL AUTO_INCREMENT,
  `b_id` int(11) DEFAULT NULL,
  `e_name` varchar(255) NOT NULL,
  `e_lat` decimal(10,8) NOT NULL,
  `e_lon` decimal(11,8) NOT NULL,
  `e_capac` int(11) DEFAULT NULL,
  `e_bandpaid` tinyint(1) DEFAULT NULL,
  `e_accepted` tinyint(1) DEFAULT NULL,
  `e_start` datetime(6) NOT NULL,
  `e_end` datetime(6) NOT NULL,
  `h_id_id` int(11) NOT NULL,
  PRIMARY KEY (`e_id`),
  KEY `polls_events_h_id_id_34da03ef_fk_polls_hosts_h_id` (`h_id_id`),
  CONSTRAINT `polls_events_h_id_id_34da03ef_fk_polls_hosts_h_id` FOREIGN KEY (`h_id_id`) REFERENCES `polls_hosts` (`h_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_events`
--

LOCK TABLES `polls_events` WRITE;
/*!40000 ALTER TABLE `polls_events` DISABLE KEYS */;
INSERT INTO `polls_events` VALUES (1,1,'Cool Party',38.04008230,-78.51999340,70,0,1,'2016-12-10 18:30:00.000000','2016-12-10 22:30:00.000000',3),(2,2,'Election Night Party',38.04008230,-78.51999340,250,1,0,'2016-12-11 19:30:00.000000','2016-12-11 23:00:00.000000',1),(3,3,'Finals Are Over Celebration',38.04008230,-78.51999340,2000,1,0,'2016-12-13 21:30:00.000000','2016-12-14 02:30:00.000000',2);
/*!40000 ALTER TABLE `polls_events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_hosts`
--

DROP TABLE IF EXISTS `polls_hosts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_hosts` (
  `h_id` int(11) NOT NULL AUTO_INCREMENT,
  `h_name` varchar(255) NOT NULL,
  `h_email` varchar(255) NOT NULL,
  `h_phone` varchar(31) NOT NULL,
  `h_availability` varchar(255) NOT NULL,
  `h_avgrating` decimal(4,3) DEFAULT NULL,
  PRIMARY KEY (`h_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_hosts`
--

LOCK TABLES `polls_hosts` WRITE;
/*!40000 ALTER TABLE `polls_hosts` DISABLE KEYS */;
INSERT INTO `polls_hosts` VALUES (1,'Charlottesville Event Hosters','ngb2zf@virginia.edu','111-999-8888','Usually available for call on Mondays 8 to 4',4.400),(2,'Albemarle County Entertainment','rjd9se@virginia.edu','998-199-2009','Call from 9 to 5 Monday through Friday',3.700),(3,'University of Virginia Student Council','jwz2kn@virginia.edu','432-765-9871','Call from 10 to 3 Tuesday through Thursday',3.100);
/*!40000 ALTER TABLE `polls_hosts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-27 20:19:55

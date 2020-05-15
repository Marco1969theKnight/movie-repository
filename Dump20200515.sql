-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: peliculas_db
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actores`
--

DROP TABLE IF EXISTS `actores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actores` (
  `id_actor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `id_alma_mater` int DEFAULT NULL,
  `anio_act_in` year NOT NULL,
  `anio_act_fin` year NOT NULL,
  PRIMARY KEY (`id_actor`),
  KEY `fk_id_alma_mater_actores` (`id_alma_mater`),
  CONSTRAINT `fk_id_alma_mater_actores` FOREIGN KEY (`id_alma_mater`) REFERENCES `alma_mater` (`id_alma_mater`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actores`
--

LOCK TABLES `actores` WRITE;
/*!40000 ALTER TABLE `actores` DISABLE KEYS */;
INSERT INTO `actores` VALUES (1,'Chadwick','Boseman',1,2000,2020),(2,'Michael','Jordan',2,1999,2020),(3,'Lupita','Nyong\'o',3,2005,2020),(4,'Charles','Chaplin',NULL,1901,1976),(5,'Paulette','Goddard',NULL,1926,1972),(6,'Henry','Bergman',NULL,1913,1936),(7,'Yalitza','Aparicio',NULL,2018,2020),(8,'Marina','de Tavara',6,1998,2020),(9,'Robert Jr.','Downey',9,1970,2020),(10,'Chris','Evans',10,1997,2020),(11,'Mark','Ruffalo',12,1989,2020);
/*!40000 ALTER TABLE `actores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alma_mater`
--

DROP TABLE IF EXISTS `alma_mater`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alma_mater` (
  `id_alma_mater` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  `id_pais` int NOT NULL,
  PRIMARY KEY (`id_alma_mater`),
  KEY `fk_id_pais` (`id_pais`),
  CONSTRAINT `fk_id_pais` FOREIGN KEY (`id_pais`) REFERENCES `pais` (`id_pais`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alma_mater`
--

LOCK TABLES `alma_mater` WRITE;
/*!40000 ALTER TABLE `alma_mater` DISABLE KEYS */;
INSERT INTO `alma_mater` VALUES (1,'Howard University',1),(2,'Newark Arts High School',1),(3,'Hampshire College',1),(4,'California State University',1),(5,'Universidad Autonoma de Mexico',2),(6,'Centro Formacion Teatral San Cayetano',2),(8,'University of Pennsylvania',1),(9,'Santa Monica High School',1),(10,'Lee Strasberg Theatre and Film Institute',1),(11,'University of Iowa',1),(12,'Stella Alder Studio of Acting',1);
/*!40000 ALTER TABLE `alma_mater` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carrera_actores`
--

DROP TABLE IF EXISTS `carrera_actores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrera_actores` (
  `id_actor` int NOT NULL,
  `id_pelicula` int NOT NULL,
  `remuneracion` float NOT NULL,
  PRIMARY KEY (`id_actor`,`id_pelicula`),
  KEY `fk_id_pelicula_carrera_actor` (`id_pelicula`),
  CONSTRAINT `fk_id_actor_carrera` FOREIGN KEY (`id_actor`) REFERENCES `actores` (`id_actor`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_id_pelicula_carrera_actor` FOREIGN KEY (`id_pelicula`) REFERENCES `peliculas` (`id_pelicula`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrera_actores`
--

LOCK TABLES `carrera_actores` WRITE;
/*!40000 ALTER TABLE `carrera_actores` DISABLE KEYS */;
INSERT INTO `carrera_actores` VALUES (1,1,1500000),(2,1,2000000),(3,1,1000000),(4,2,100000),(5,2,50000),(6,2,50000),(7,3,100000),(8,3,200000),(9,4,1200000),(10,4,1200000),(11,4,1200000);
/*!40000 ALTER TABLE `carrera_actores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carrera_escritores`
--

DROP TABLE IF EXISTS `carrera_escritores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrera_escritores` (
  `id_escritor` int NOT NULL,
  `id_pelicula` int NOT NULL,
  `remuneracion` float NOT NULL,
  PRIMARY KEY (`id_escritor`,`id_pelicula`),
  KEY `fk_id_pelicula_escritor_carrera` (`id_pelicula`),
  CONSTRAINT `fk_id_escritor_carrera` FOREIGN KEY (`id_escritor`) REFERENCES `escritores` (`id_escritor`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_id_pelicula_escritor_carrera` FOREIGN KEY (`id_pelicula`) REFERENCES `peliculas` (`id_pelicula`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrera_escritores`
--

LOCK TABLES `carrera_escritores` WRITE;
/*!40000 ALTER TABLE `carrera_escritores` DISABLE KEYS */;
INSERT INTO `carrera_escritores` VALUES (1,1,2500000),(2,2,100000),(3,3,1000000),(4,4,2500000),(5,4,2500000);
/*!40000 ALTER TABLE `carrera_escritores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `directores`
--

DROP TABLE IF EXISTS `directores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `directores` (
  `id_director` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `id_alma_mater` int DEFAULT NULL,
  `anio_act_in` year NOT NULL,
  `anio_act_fin` year NOT NULL,
  PRIMARY KEY (`id_director`),
  KEY `fk_id_alma_mater_directores` (`id_alma_mater`),
  CONSTRAINT `fk_id_alma_mater_directores` FOREIGN KEY (`id_alma_mater`) REFERENCES `alma_mater` (`id_alma_mater`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `directores`
--

LOCK TABLES `directores` WRITE;
/*!40000 ALTER TABLE `directores` DISABLE KEYS */;
INSERT INTO `directores` VALUES (1,'Ryan','Coogler',4,2009,2020),(2,'Charles','Chaplin',NULL,1901,1976),(3,'Alfonso','Cuaron',5,1981,2020),(5,'Juan','Perez',5,1980,2020),(6,'Anthony','Russo',8,1994,2020);
/*!40000 ALTER TABLE `directores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `escritores`
--

DROP TABLE IF EXISTS `escritores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `escritores` (
  `id_escritor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `id_alma_mater` int DEFAULT NULL,
  `anio_act_in` year NOT NULL,
  `anio_act_fin` year NOT NULL,
  PRIMARY KEY (`id_escritor`),
  KEY `fk_id_alma_mater_escrirotes` (`id_alma_mater`),
  CONSTRAINT `fk_id_alma_mater_escrirotes` FOREIGN KEY (`id_alma_mater`) REFERENCES `alma_mater` (`id_alma_mater`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `escritores`
--

LOCK TABLES `escritores` WRITE;
/*!40000 ALTER TABLE `escritores` DISABLE KEYS */;
INSERT INTO `escritores` VALUES (1,'Ryan','Coogler',4,2009,2020),(2,'Charles','Chaplin',NULL,1901,1976),(3,'Alfonso','Cuaron',5,1981,2020),(4,'Joseph','Russo',11,1994,2020),(5,'Anthony','Russo',8,1994,2020);
/*!40000 ALTER TABLE `escritores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genero`
--

DROP TABLE IF EXISTS `genero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genero` (
  `id_genero` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `sub_gen` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_genero`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genero`
--

LOCK TABLES `genero` WRITE;
/*!40000 ALTER TABLE `genero` DISABLE KEYS */;
INSERT INTO `genero` VALUES (1,'Accion','Super Heroes'),(2,'Aventura','Exploracion'),(3,'Experimental','Indie'),(4,'Familiar','Animales'),(5,'Comedia','Critica social'),(6,'Drama','Tragedia');
/*!40000 ALTER TABLE `genero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pais`
--

DROP TABLE IF EXISTS `pais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pais` (
  `id_pais` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  PRIMARY KEY (`id_pais`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pais`
--

LOCK TABLES `pais` WRITE;
/*!40000 ALTER TABLE `pais` DISABLE KEYS */;
INSERT INTO `pais` VALUES (1,'Estados Unidos de America'),(2,'Mexico lindo'),(3,'Canada'),(5,'Guatemala');
/*!40000 ALTER TABLE `pais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peliculas`
--

DROP TABLE IF EXISTS `peliculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `peliculas` (
  `id_pelicula` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(40) NOT NULL,
  `id_genero` int NOT NULL,
  `id_director` int NOT NULL,
  `anio` year NOT NULL,
  `id_pais` int DEFAULT NULL,
  `calif` int NOT NULL,
  PRIMARY KEY (`id_pelicula`),
  KEY `fk_id_genero` (`id_genero`),
  KEY `fk_id_director` (`id_director`),
  KEY `fk_id_pais_peliculas` (`id_pais`),
  CONSTRAINT `fk_id_director` FOREIGN KEY (`id_director`) REFERENCES `directores` (`id_director`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_id_genero` FOREIGN KEY (`id_genero`) REFERENCES `genero` (`id_genero`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_id_pais_peliculas` FOREIGN KEY (`id_pais`) REFERENCES `pais` (`id_pais`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peliculas`
--

LOCK TABLES `peliculas` WRITE;
/*!40000 ALTER TABLE `peliculas` DISABLE KEYS */;
INSERT INTO `peliculas` VALUES (1,'Black panther',1,1,2018,1,97),(2,'Modern times',5,2,1936,1,100),(3,'Roma',6,3,2018,2,95),(4,'Advengers Endgame',1,6,2019,1,93);
/*!40000 ALTER TABLE `peliculas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-15 13:56:56

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actores`
--

LOCK TABLES `actores` WRITE;
/*!40000 ALTER TABLE `actores` DISABLE KEYS */;
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
  `nombre` varchar(35) NOT NULL,
  `id_pais` int NOT NULL,
  PRIMARY KEY (`id_alma_mater`),
  KEY `fk_id_pais` (`id_pais`),
  CONSTRAINT `fk_id_pais` FOREIGN KEY (`id_pais`) REFERENCES `pais` (`id_pais`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alma_mater`
--

LOCK TABLES `alma_mater` WRITE;
/*!40000 ALTER TABLE `alma_mater` DISABLE KEYS */;
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
  CONSTRAINT `fk_id_actor_carrera` FOREIGN KEY (`id_actor`) REFERENCES `escritores` (`id_escritor`),
  CONSTRAINT `fk_id_pelicula_carrera_actor` FOREIGN KEY (`id_pelicula`) REFERENCES `peliculas` (`id_pelicula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrera_actores`
--

LOCK TABLES `carrera_actores` WRITE;
/*!40000 ALTER TABLE `carrera_actores` DISABLE KEYS */;
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
  CONSTRAINT `fk_id_escritor_carrera` FOREIGN KEY (`id_escritor`) REFERENCES `escritores` (`id_escritor`),
  CONSTRAINT `fk_id_pelicula_escritor_carrera` FOREIGN KEY (`id_pelicula`) REFERENCES `peliculas` (`id_pelicula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrera_escritores`
--

LOCK TABLES `carrera_escritores` WRITE;
/*!40000 ALTER TABLE `carrera_escritores` DISABLE KEYS */;
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
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(30) NOT NULL,
  `id_alma_mater` int DEFAULT NULL,
  `anio_act_in` year NOT NULL,
  `anio_act_fin` year NOT NULL,
  PRIMARY KEY (`id_director`),
  KEY `fk_id_alma_mater_directores` (`id_alma_mater`),
  CONSTRAINT `fk_id_alma_mater_directores` FOREIGN KEY (`id_alma_mater`) REFERENCES `alma_mater` (`id_alma_mater`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `directores`
--

LOCK TABLES `directores` WRITE;
/*!40000 ALTER TABLE `directores` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `escritores`
--

LOCK TABLES `escritores` WRITE;
/*!40000 ALTER TABLE `escritores` DISABLE KEYS */;
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
  `nombre` varchar(25) NOT NULL,
  `sub_gen` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id_genero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genero`
--

LOCK TABLES `genero` WRITE;
/*!40000 ALTER TABLE `genero` DISABLE KEYS */;
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
  `nombre` varchar(25) NOT NULL,
  PRIMARY KEY (`id_pais`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pais`
--

LOCK TABLES `pais` WRITE;
/*!40000 ALTER TABLE `pais` DISABLE KEYS */;
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
  `titulo` varchar(30) NOT NULL,
  `id_genero` int DEFAULT NULL,
  `id_director` int DEFAULT NULL,
  `anio` year NOT NULL,
  `id_pais` int NOT NULL,
  `calif` int NOT NULL,
  PRIMARY KEY (`id_pelicula`),
  KEY `fk_id_genero` (`id_genero`),
  KEY `fk_id_director` (`id_director`),
  KEY `fk_id_pais_peliculas` (`id_pais`),
  CONSTRAINT `fk_id_director` FOREIGN KEY (`id_director`) REFERENCES `directores` (`id_director`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_id_genero` FOREIGN KEY (`id_genero`) REFERENCES `genero` (`id_genero`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_id_pais_peliculas` FOREIGN KEY (`id_pais`) REFERENCES `pais` (`id_pais`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peliculas`
--

LOCK TABLES `peliculas` WRITE;
/*!40000 ALTER TABLE `peliculas` DISABLE KEYS */;
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

-- Dump completed on 2020-04-12 16:35:49

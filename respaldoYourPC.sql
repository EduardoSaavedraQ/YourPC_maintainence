-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: yourpc
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `componentes`
--

DROP TABLE IF EXISTS `componentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `componentes` (
  `pk_nombre` varchar(255) NOT NULL,
  `fk_id_admin` varchar(255) DEFAULT NULL,
  `descripcion` text NOT NULL,
  `imagen` blob,
  PRIMARY KEY (`pk_nombre`),
  KEY `fk_id_admin` (`fk_id_admin`),
  CONSTRAINT `componentes_ibfk_1` FOREIGN KEY (`fk_id_admin`) REFERENCES `usuarios` (`pk_nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `componentes`
--

LOCK TABLES `componentes` WRITE;
/*!40000 ALTER TABLE `componentes` DISABLE KEYS */;
/*!40000 ALTER TABLE `componentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libretas`
--

DROP TABLE IF EXISTS `libretas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libretas` (
  `pk_id_libreta` int NOT NULL,
  `fk_id_usuario` varchar(255) DEFAULT NULL,
  `descripcion` text,
  `fecha_creacion` date DEFAULT NULL,
  PRIMARY KEY (`pk_id_libreta`),
  KEY `fk_id_usuario` (`fk_id_usuario`),
  CONSTRAINT `libretas_ibfk_1` FOREIGN KEY (`fk_id_usuario`) REFERENCES `usuarios` (`pk_nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libretas`
--

LOCK TABLES `libretas` WRITE;
/*!40000 ALTER TABLE `libretas` DISABLE KEYS */;
/*!40000 ALTER TABLE `libretas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libretas_componentes`
--

DROP TABLE IF EXISTS `libretas_componentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libretas_componentes` (
  `fk_id_libreta` int NOT NULL,
  `fk_id_componente` varchar(255) NOT NULL,
  PRIMARY KEY (`fk_id_libreta`,`fk_id_componente`),
  KEY `fk_id_componente` (`fk_id_componente`),
  CONSTRAINT `libretas_componentes_ibfk_1` FOREIGN KEY (`fk_id_libreta`) REFERENCES `libretas` (`pk_id_libreta`),
  CONSTRAINT `libretas_componentes_ibfk_2` FOREIGN KEY (`fk_id_componente`) REFERENCES `componentes` (`pk_nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libretas_componentes`
--

LOCK TABLES `libretas_componentes` WRITE;
/*!40000 ALTER TABLE `libretas_componentes` DISABLE KEYS */;
/*!40000 ALTER TABLE `libretas_componentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `fk_nombre_componente` varchar(255) DEFAULT NULL,
  `link` varchar(255) NOT NULL,
  `precio` float NOT NULL,
  KEY `fk_nombre_componente` (`fk_nombre_componente`),
  CONSTRAINT `proveedores_ibfk_1` FOREIGN KEY (`fk_nombre_componente`) REFERENCES `componentes` (`pk_nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `pk_nickname` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `contrasenia` varchar(255) NOT NULL,
  `fecha_registro` date NOT NULL,
  `admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`pk_nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-14 15:19:52

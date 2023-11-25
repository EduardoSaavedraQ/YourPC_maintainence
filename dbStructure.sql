-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: yourpclb1
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
-- Table structure for table `pc`
--

DROP TABLE IF EXISTS `pc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pc` (
  `pk_nombre` varchar(255) NOT NULL,
  `fk_id_admin` varchar(255) DEFAULT NULL,
  `descripcion` text NOT NULL,
  `precio` float NOT NULL,
  `proposito` tinyint(1) DEFAULT NULL,
  `imagen_filename` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`pk_nombre`),
  KEY `fk_id_admin` (`fk_id_admin`),
  CONSTRAINT `pc_ibfk_1` FOREIGN KEY (`fk_id_admin`) REFERENCES `usuarios` (`pk_nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pc`
--

LOCK TABLES `pc` WRITE;
/*!40000 ALTER TABLE `pc` DISABLE KEYS */;
INSERT INTO `pc` VALUES ('Cpu Computadora Edicion Video 4k','root','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nulla facere sapiente aperiam et, adipisci illum maiores officia? Repellendus ullam dolor omnis quos, obcaecati quam veniam voluptates corrupti deleniti officiis?',17900,1,'D_NQ_NP_2X_972293-MLM26715384231.jpg'),('Cpue Completo Dell Optiplex','root','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nulla facere sapiente aperiam et, adipisci illum maiores officia? Repellendus ullam dolor omnis quos, obcaecati quam veniam voluptates corrupti deleniti officiis?',3500,1,'D_NQ_NP_2X_864870-MLM70916440233.jpg'),('Laptop Chuwi HeroBook Pro space gray 14.1\", Intel Celeron N4020 8GB de RAM 256GB SSD, Intel UHD Graphics 600 1920x1080px Windows 11 Home','root','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nulla facere sapiente aperiam et, adipisci illum maiores officia? Repellendus ullam dolor omnis quos, obcaecati quam veniam voluptates corrupti deleniti officiis?',5977.93,1,'D_NQ_NP_2X_723065-MLA46169085812.png'),('Laptop HP 14-FQ1025cl azul táctil AMD Ryzen 7 16GB de RAM 512GB SSD, AMD Radeon Graphics Windows 11 Home\", Intel Celeron N4020 8GB de RAM 256GB SSD, Intel UHD Graphics 600 1920x1080px Windows 11 Home','root','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nulla facere sapiente aperiam et, adipisci illum maiores officia? Repellendus ullam dolor omnis quos, obcaecati quam veniam voluptates corrupti deleniti officiis?',16999,2,'D_NQ_NP_2X_819454-MLU71429261050.jpg'),('MacBook Air A1932 (True Tone 2019) gris espacial 13\"','root','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nulla facere sapiente aperiam et, adipisci illum maiores officia? Repellendus ullam dolor omnis quos, obcaecati quam veniam voluptates corrupti deleniti officiis?',16824,3,'D_NQ_NP_2X_812710-MLA45106324152.jpg'),('Microsoft Surface Studio 2+ 28 1tb 32gb I7 Nvidia Rtx 3060','root','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nulla facere sapiente aperiam et, adipisci illum maiores officia? Repellendus ullam dolor omnis quos, obcaecati quam veniam voluptates corrupti deleniti officiis?',166248,4,'D_NQ_NP_2X_664744-MLM54248142246.jpg'),('PC de prueba','nuevoAdmin1','Descripción de prueba',50,1,'OIP.jpeg'),('PC de prueba 2','nuevoAdmin1','Descripción de prueba 2',5000,2,'GO_DIEGO_GO.jpeg'),('Pc Gamer Cpu Amd 5600g Ram 32gb Ddr4 240gb Ssd Hdd 2 Tb','root','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nulla facere sapiente aperiam et, adipisci illum maiores officia? Repellendus ullam dolor omnis quos, obcaecati quam veniam voluptates corrupti deleniti officiis?',8899,3,'D_NQ_NP_2X_697535-MLM72046790223.jpg'),('Pc Intel Gold Wifi Oficina 8gb Ram Ssd 500gb Monitor 19 Kit','root','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nulla facere sapiente aperiam et, adipisci illum maiores officia? Repellendus ullam dolor omnis quos, obcaecati quam veniam voluptates corrupti deleniti officiis?',7500,1,'D_NQ_NP_2X_751818-MLM54968213244.jpg'),('Rtx4060 Laptop Gamer Ryzen 7 7735h Machenike L16pro 16g 1t','root','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nulla facere sapiente aperiam et, adipisci illum maiores officia? Repellendus ullam dolor omnis quos, obcaecati quam veniam voluptates corrupti deleniti officiis?',22788.3,3,'D_NQ_NP_2X_969273-CBT72457838654.jpg'),('Xtreme Pc Xpg Geforce Rtx 4080 I9 13900kf 32gb Ddr5 Ssd 2tb','root','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis nulla facere sapiente aperiam et, adipisci illum maiores officia? Repellendus ullam dolor omnis quos, obcaecati quam veniam voluptates corrupti deleniti officiis?',51539.4,4,'D_NQ_NP_2X_783081-MLM70460919214.jpg');
/*!40000 ALTER TABLE `pc` ENABLE KEYS */;
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
  `fecha_registro` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `admin` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`pk_nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES ('nuevoAdmin1','nuevoAdmin1@admin.com','pbkdf2:sha256:260000$h59lATlSe1cnlYq5$75dd7497d63e9c6871f51e3030b328e0b53887ada8c6c0b59c5881dff35830f9','2023-11-20 23:54:44',1),('Prueba','123456@prueba.com','pbkdf2:sha256:260000$Wg3iAtLW6Vb3rkBY$575529ab360e31584370a4a1f87fc3759f7dddf438b60d440dfe9bb3d1ce0e76','2023-10-28 13:43:39',0),('root','eduardoooo89@hotmail.com','pbkdf2:sha256:260000$dGA38dIpdUn57vEh$ca0ffefe53b25c90d3a5d822f59e2891bd881f83219ed4ae28aedae55bd057be','2023-10-25 09:46:48',1);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_pcs`
--

DROP TABLE IF EXISTS `usuarios_pcs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_pcs` (
  `fk_id_usuario` varchar(255) NOT NULL,
  `fk_id_pc` varchar(255) NOT NULL,
  KEY `fk_id_usuario` (`fk_id_usuario`),
  KEY `fk_id_pc` (`fk_id_pc`),
  CONSTRAINT `usuarios_pcs_ibfk_1` FOREIGN KEY (`fk_id_usuario`) REFERENCES `usuarios` (`pk_nickname`),
  CONSTRAINT `usuarios_pcs_ibfk_2` FOREIGN KEY (`fk_id_pc`) REFERENCES `pc` (`pk_nombre`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_pcs`
--

LOCK TABLES `usuarios_pcs` WRITE;
/*!40000 ALTER TABLE `usuarios_pcs` DISABLE KEYS */;
INSERT INTO `usuarios_pcs` VALUES ('nuevoAdmin1','Cpu Computadora Edicion Video 4k'),('nuevoAdmin1','Cpue Completo Dell Optiplex'),('nuevoAdmin1','PC de prueba'),('nuevoAdmin1','PC de prueba 2'),('Prueba','Cpu Computadora Edicion Video 4k'),('Prueba','PC de prueba'),('Prueba','PC de prueba 2'),('root','PC de prueba'),('nuevoAdmin1','Laptop HP 14-FQ1025cl azul táctil AMD Ryzen 7 16GB de RAM 512GB SSD, AMD Radeon Graphics Windows 11 Home\", Intel Celeron N4020 8GB de RAM 256GB SSD, Intel UHD Graphics 600 1920x1080px Windows 11 Home'),('nuevoAdmin1','Rtx4060 Laptop Gamer Ryzen 7 7735h Machenike L16pro 16g 1t'),('nuevoAdmin1','Microsoft Surface Studio 2+ 28 1tb 32gb I7 Nvidia Rtx 3060'),('Prueba','Laptop HP 14-FQ1025cl azul táctil AMD Ryzen 7 16GB de RAM 512GB SSD, AMD Radeon Graphics Windows 11 Home\", Intel Celeron N4020 8GB de RAM 256GB SSD, Intel UHD Graphics 600 1920x1080px Windows 11 Home'),('Prueba','Xtreme Pc Xpg Geforce Rtx 4080 I9 13900kf 32gb Ddr5 Ssd 2tb'),('Prueba','Pc Intel Gold Wifi Oficina 8gb Ram Ssd 500gb Monitor 19 Kit'),('root','Laptop Chuwi HeroBook Pro space gray 14.1\", Intel Celeron N4020 8GB de RAM 256GB SSD, Intel UHD Graphics 600 1920x1080px Windows 11 Home'),('root','Rtx4060 Laptop Gamer Ryzen 7 7735h Machenike L16pro 16g 1t'),('root','Microsoft Surface Studio 2+ 28 1tb 32gb I7 Nvidia Rtx 3060'),('root','Pc Gamer Cpu Amd 5600g Ram 32gb Ddr4 240gb Ssd Hdd 2 Tb'),('root','Cpu Computadora Edicion Video 4k');
/*!40000 ALTER TABLE `usuarios_pcs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-25  9:34:31

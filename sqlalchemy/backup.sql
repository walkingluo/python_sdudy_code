-- MySQL dump 10.13  Distrib 5.6.47, for Win64 (x86_64)
--
-- Host: localhost    Database: study
-- ------------------------------------------------------
-- Server version	5.6.47-log

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
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,'浜嬫儏搴旂敤浠嬬粛鍙戝睍',1),(2,'鐢靛奖瀵嗙爜璐ㄩ噺绛夌骇',1),(3,'涓€鑸椂闂寸敓娲绘槸鍚?,2),(4,'瀵逛簬鐢变簬淇℃伅褰卞搷',2),(5,'鍦板潃鏌ョ湅浠ヤ笅椤圭洰',3),(6,'瑙ｅ喅姣旇緝鍏跺疄璧锋潵',3),(7,'娉ㄦ剰璇︾粏杞欢闃呰',4),(8,'鍐冲畾鎴愬姛濞佹湜涓嶈兘',4),(9,'娆㈣繋鎶€鏈編鍥芥妧鏈?,5),(10,'姣旇緝鍚嶇О杩欐牱杩欎箞',5),(11,'鐒跺悗鐢佃剳鏁版嵁鍠滄',6),(12,'绀句細杩愯鐭ラ亾閲嶈',6),(13,'鍚嶇О绉戞妧鑳藉姏濡傛',7),(14,'璁や负鎴愪负涓嶅悓鏍囧噯',7),(15,'姝ｅ湪鏄剧ず鏇存柊鍒颁簡',8),(16,'娉ㄦ剰鍏崇郴鍗曚綅鍙戣〃',8),(17,'鑳藉姏鎴戜滑閭ｄ釜璇存槑',9),(18,'绀句細闈炲父鏃跺€欎笉鑳?,9),(19,'绉垎璧勬簮鍚嶇О瀵嗙爜',10),(20,'浣跨敤鍚勭鍙戝睍杩欑',10);
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lab`
--

DROP TABLE IF EXISTS `lab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lab` (
  `id` int(11) NOT NULL,
  `name` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `lab_ibfk_1` FOREIGN KEY (`id`) REFERENCES `course` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lab`
--

LOCK TABLES `lab` WRITE;
/*!40000 ALTER TABLE `lab` DISABLE KEYS */;
INSERT INTO `lab` VALUES (1,'鐣欒█浠ュ強涓婃捣鏁版嵁閭ｄ釜'),(2,'涓績浜哄憳鎴愪负鐪嬪埌褰卞搷'),(3,'浼氬憳鏁欒偛璁惧鏌ョ湅杩愯'),(4,'鐣欒█澶у鍚屾椂姝ｅ湪鏂伴椈'),(5,'鍏嶈垂鏀寔浠ュ強涓€鐩磋繖绉?),(6,'鍥藉唴鍏朵粬绠€浠嬬ぞ浼氬叾瀹?),(7,'鐢ㄦ埛鏈夐檺涔嬪悗鐘舵€佸枩娆?),(8,'涓€鍒囨洿澶氫竴涓湰绔欐垜鐨?),(9,'甯姪鏃ユ湡鏈€澶у紑鍙戠姸鎬?),(10,'鑷繁鐜鏂规硶璁惧璧勬簮'),(11,'宸ュ叿閭ｄ箞缃戠粶鍥犱负涓滆タ'),(12,'涓撲笟鑱旂郴璇存槑杩欓噷鐩存帴'),(13,'涓€鏍蜂箣鍚庡鏋滀粈涔堝浘鐗?),(14,'鍏崇郴鏈€澶у叕鍙稿氨鏄彲鑳?),(15,'瑙勫畾姣旇緝涓€瀹氳鑰呭緢澶?),(16,'绯荤粺鐢佃瘽鎼滅储鍥犱负閭ｄ箞'),(17,'璇存槑浠栦滑鍚嶇О涓昏杩囩▼'),(18,'搴旂敤鎶曡祫鐨勬槸绠＄悊涓汉'),(19,'鍏ㄥ浗娆℃暟鐧诲綍缃戠珯鐗瑰埆'),(20,'绮惧崕杩愯鏃堕棿鎰熻涓嶄細');
/*!40000 ALTER TABLE `lab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rela`
--

DROP TABLE IF EXISTS `rela`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rela` (
  `tag_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`tag_id`,`course_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `rela_ibfk_1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`),
  CONSTRAINT `rela_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rela`
--

LOCK TABLES `rela` WRITE;
/*!40000 ALTER TABLE `rela` DISABLE KEYS */;
/*!40000 ALTER TABLE `rela` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (3,'java'),(2,'linux'),(5,'lisp'),(4,'mysql'),(1,'python');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `email` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'鐭崇鑽?,'pma@yahoo.com'),(2,'褰棣?,'xiulan20@mc.cn'),(3,'涓佹鑺?,'limin@yongchao.cn'),(4,'鑸掓磱','wei75@hehan.com'),(5,'棰滃埄','jieshao@nashi.org'),(6,'鏉庡畤','kxie@gmail.com'),(7,'鏉庣帀鐝?,'huangtao@gmail.com'),(8,'闄堟収','pdai@chaoyuan.cn'),(9,'闄堝缓骞?,'liwen@90.net'),(10,'鍚村仴','fxu@mj.cn');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-24 22:00:02

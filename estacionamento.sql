-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 16, 2021 at 05:55 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `estacionamento`
--

-- --------------------------------------------------------

--
-- Table structure for table `lugares`
--

CREATE TABLE `lugares` (
  `id` int(11) NOT NULL,
  `lugar` int(11) DEFAULT NULL,
  `matricula` varchar(20) DEFAULT NULL,
  `hora_entrada` datetime DEFAULT NULL,
  `hora_saida` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lugares`
--

INSERT INTO `lugares` (`id`, `lugar`, `matricula`, `hora_entrada`, `hora_saida`) VALUES
(1, 19, '20-GA-21', '2021-11-09 15:18:27', '2021-11-09 16:56:57'),
(4, 4, '30-BO-21', '2021-11-09 16:20:41', '2021-11-09 17:30:21'),
(5, 6, '30-TW-41', '2021-11-09 15:22:23', NULL),
(6, 30, '30-GA-20', '2021-11-09 15:27:41', '2021-11-09 16:51:42'),
(7, 5, '20-WW-20', '2021-11-09 15:28:51', '2021-11-09 17:14:45'),
(8, 7, '93-MV-21', '2021-11-09 17:02:29', NULL),
(9, 3, '30-WX-21', '2021-11-09 17:02:43', '2021-11-09 17:22:10'),
(10, 8, '20-GA-76', '2021-11-16 14:25:55', NULL),
(12, 10, '65-42-XX', '2021-11-16 15:15:59', NULL),
(13, 22, '65-OP-91', '2021-11-16 15:26:56', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `lugares`
--
ALTER TABLE `lugares`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `lugares`
--
ALTER TABLE `lugares`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

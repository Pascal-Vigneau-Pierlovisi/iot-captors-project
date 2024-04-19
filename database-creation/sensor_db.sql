-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:8889
-- Généré le : ven. 19 avr. 2024 à 07:06
-- Version du serveur : 5.7.39
-- Version de PHP : 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `sensor_db`
--

-- --------------------------------------------------------

--
-- Structure de la table `sensor_data`
--

CREATE TABLE `sensor_data` (
  `id` int(11) NOT NULL,
  `topic` varchar(255) DEFAULT NULL,
  `payload` varchar(255) DEFAULT NULL,
  `received_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `sensor_humidity`
--

CREATE TABLE `sensor_humidity` (
  `id` int(11) NOT NULL,
  `topic` varchar(255) DEFAULT NULL,
  `payload` varchar(255) DEFAULT NULL,
  `received_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `sensor_humidity`
--

INSERT INTO `sensor_humidity` (`id`, `topic`, `payload`, `received_at`) VALUES
(2460, 'humidity', '37', '2024-04-18 14:35:04'),
(2461, 'humidity', '38', '2024-04-18 14:35:14'),
(2462, 'humidity', '37', '2024-04-18 14:35:26'),
(2463, 'humidity', '38', '2024-04-18 14:35:34'),
(2464, 'humidity', '38', '2024-04-18 14:35:45'),
(2465, 'humidity', '37', '2024-04-18 14:35:55'),
(2466, 'humidity', '38', '2024-04-18 14:36:05'),
(2467, 'humidity', '37', '2024-04-18 14:36:16'),
(2468, 'humidity', '38', '2024-04-18 14:36:26'),
(2469, 'humidity', '37', '2024-04-18 14:36:36'),
(2470, 'humidity', '37', '2024-04-18 14:36:46'),
(2471, 'humidity', '38', '2024-04-18 14:36:57'),
(2472, 'humidity', '37', '2024-04-18 14:37:07'),
(2473, 'humidity', '38', '2024-04-18 14:37:17'),
(2474, 'humidity', '37', '2024-04-18 14:37:28'),
(2475, 'humidity', '38', '2024-04-18 14:37:38'),
(2476, 'humidity', '37', '2024-04-18 14:37:48'),
(2477, 'humidity', '38', '2024-04-18 14:37:59'),
(2478, 'humidity', '37', '2024-04-18 14:38:09'),
(2479, 'humidity', '37', '2024-04-18 14:38:19'),
(2480, 'humidity', '38', '2024-04-18 14:38:29'),
(2481, 'humidity', '37', '2024-04-18 14:38:40'),
(2482, 'humidity', '38', '2024-04-18 14:38:50'),
(2483, 'humidity', '37', '2024-04-18 14:39:00'),
(2484, 'humidity', '38', '2024-04-18 14:39:11'),
(2485, 'humidity', '37', '2024-04-18 14:39:21'),
(2486, 'humidity', '37', '2024-04-18 14:39:31'),
(2487, 'humidity', '38', '2024-04-18 14:39:41'),
(2488, 'humidity', '37', '2024-04-18 14:39:52'),
(2489, 'humidity', '38', '2024-04-18 14:40:02');

-- --------------------------------------------------------

--
-- Structure de la table `sensor_sound`
--

CREATE TABLE `sensor_sound` (
  `id` int(11) NOT NULL,
  `topic` varchar(255) DEFAULT NULL,
  `payload` varchar(255) DEFAULT NULL,
  `received_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `sensor_sound`
--

INSERT INTO `sensor_sound` (`id`, `topic`, `payload`, `received_at`) VALUES
(2460, 'sound', '5', '2024-04-18 14:35:04'),
(2461, 'sound', '6', '2024-04-18 14:35:14'),
(2462, 'sound', '7', '2024-04-18 14:35:26'),
(2463, 'sound', '4', '2024-04-18 14:35:34'),
(2464, 'sound', '0', '2024-04-18 14:35:45'),
(2465, 'sound', '3', '2024-04-18 14:35:55'),
(2466, 'sound', '0', '2024-04-18 14:36:05'),
(2467, 'sound', '0', '2024-04-18 14:36:16'),
(2468, 'sound', '0', '2024-04-18 14:36:26'),
(2469, 'sound', '0', '2024-04-18 14:36:36'),
(2470, 'sound', '0', '2024-04-18 14:36:46'),
(2471, 'sound', '0', '2024-04-18 14:36:57'),
(2472, 'sound', '0', '2024-04-18 14:37:07'),
(2473, 'sound', '0', '2024-04-18 14:37:17'),
(2474, 'sound', '0', '2024-04-18 14:37:28'),
(2475, 'sound', '0', '2024-04-18 14:37:38'),
(2476, 'sound', '15', '2024-04-18 14:37:48'),
(2477, 'sound', '0', '2024-04-18 14:37:59'),
(2478, 'sound', '2', '2024-04-18 14:38:09'),
(2479, 'sound', '0', '2024-04-18 14:38:19'),
(2480, 'sound', '27', '2024-04-18 14:38:29'),
(2481, 'sound', '0', '2024-04-18 14:38:40'),
(2482, 'sound', '12', '2024-04-18 14:38:50'),
(2483, 'sound', '0', '2024-04-18 14:39:00'),
(2484, 'sound', '0', '2024-04-18 14:39:11'),
(2485, 'sound', '2', '2024-04-18 14:39:21'),
(2486, 'sound', '0', '2024-04-18 14:39:31'),
(2487, 'sound', '1', '2024-04-18 14:39:41'),
(2488, 'sound', '0', '2024-04-18 14:39:52'),
(2489, 'sound', '129', '2024-04-18 14:40:02');

-- --------------------------------------------------------

--
-- Structure de la table `sensor_temp`
--

CREATE TABLE `sensor_temp` (
  `id` int(11) NOT NULL,
  `topic` varchar(255) DEFAULT NULL,
  `payload` varchar(255) DEFAULT NULL,
  `received_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `sensor_temp`
--

INSERT INTO `sensor_temp` (`id`, `topic`, `payload`, `received_at`) VALUES
(2460, 'temp', '23', '2024-04-18 14:35:04'),
(2461, 'temp', '24', '2024-04-18 14:35:14'),
(2462, 'temp', '23', '2024-04-18 14:35:26'),
(2463, 'temp', '23', '2024-04-18 14:35:34'),
(2464, 'temp', '23', '2024-04-18 14:35:45'),
(2465, 'temp', '23', '2024-04-18 14:35:55'),
(2466, 'temp', '24', '2024-04-18 14:36:05'),
(2467, 'temp', '23', '2024-04-18 14:36:16'),
(2468, 'temp', '24', '2024-04-18 14:36:26'),
(2469, 'temp', '23', '2024-04-18 14:36:36'),
(2470, 'temp', '23', '2024-04-18 14:36:46'),
(2471, 'temp', '23', '2024-04-18 14:36:57'),
(2472, 'temp', '23', '2024-04-18 14:37:07'),
(2473, 'temp', '23', '2024-04-18 14:37:17'),
(2474, 'temp', '23', '2024-04-18 14:37:28'),
(2475, 'temp', '23', '2024-04-18 14:37:38'),
(2476, 'temp', '23', '2024-04-18 14:37:48'),
(2477, 'temp', '24', '2024-04-18 14:37:59'),
(2478, 'temp', '23', '2024-04-18 14:38:09'),
(2479, 'temp', '23', '2024-04-18 14:38:19'),
(2480, 'temp', '23', '2024-04-18 14:38:29'),
(2481, 'temp', '23', '2024-04-18 14:38:40'),
(2482, 'temp', '24', '2024-04-18 14:38:50'),
(2483, 'temp', '23', '2024-04-18 14:39:00'),
(2484, 'temp', '23', '2024-04-18 14:39:11'),
(2485, 'temp', '23', '2024-04-18 14:39:21'),
(2486, 'temp', '23', '2024-04-18 14:39:31'),
(2487, 'temp', '23', '2024-04-18 14:39:41'),
(2488, 'temp', '23', '2024-04-18 14:39:52'),
(2489, 'temp', '23', '2024-04-18 14:40:02');

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(150) NOT NULL,
  `is_admin` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `is_admin`) VALUES
(1, 'pascalthetrlol', 'd57837950fc6b5faca1da86e252cfcb7fd14437a96122bb3bb25e5804d173837', NULL);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `sensor_data`
--
ALTER TABLE `sensor_data`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `sensor_humidity`
--
ALTER TABLE `sensor_humidity`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `sensor_sound`
--
ALTER TABLE `sensor_sound`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `sensor_temp`
--
ALTER TABLE `sensor_temp`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `sensor_data`
--
ALTER TABLE `sensor_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3652;

--
-- AUTO_INCREMENT pour la table `sensor_humidity`
--
ALTER TABLE `sensor_humidity`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2490;

--
-- AUTO_INCREMENT pour la table `sensor_sound`
--
ALTER TABLE `sensor_sound`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2490;

--
-- AUTO_INCREMENT pour la table `sensor_temp`
--
ALTER TABLE `sensor_temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2490;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

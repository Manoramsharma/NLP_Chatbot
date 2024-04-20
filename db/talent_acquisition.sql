CREATE DATABASE IF NOT EXISTS `talent_acquisition_platform` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `talent_acquisition_platform`;

-- Table structure for table `job_listings`
DROP TABLE IF EXISTS `job_listings`;
CREATE TABLE `job_listings` (
  `job_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `description` text,
  `requirements` text,
  `location` varchar(255) DEFAULT NULL,
  `salary` decimal(10,2),
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Sample data for table `job_listings`
INSERT INTO `job_listings` (title, description, requirements, location, salary) VALUES
('Software Developer', 'Develop and maintain software applications.', 'Proficient in coding.', 'Remote', 70000.00),
('Data Analyst', 'Analyze data sets and generate reports.', 'Experience with SQL and Python.', 'New York', 65000.00),
('Product Manager', 'Lead product development initiatives.', 'Strong leadership skills.', 'California', 90000.00);

-- Table structure for table `event_registrations`
DROP TABLE IF EXISTS `event_registrations`;
CREATE TABLE `event_registrations` (
  `registration_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `event_name` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT 'pending',
  PRIMARY KEY (`registration_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Sample data for table `event_registrations`
INSERT INTO `event_registrations` (user_id, event_name, status) VALUES
(1, 'CodeFest', 'registered'),
(2, 'Designathon', 'registered');

-- Table structure for table `user_progress`
DROP TABLE IF EXISTS `user_progress`;
CREATE TABLE `user_progress` (
  `progress_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `event_name` varchar(255) DEFAULT NULL,
  `progress` varchar(255) DEFAULT 'not started',
  PRIMARY KEY (`progress_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Sample data for table `user_progress`
INSERT INTO `user_progress` (user_id, event_name, progress) VALUES
(1, 'CodeFest', 'completed'),
(2, 'Designathon', 'in progress');

-- You can add additional tables, fields, and data as required for the recruitment platform.

-- Add any functions or stored procedures if necessary for your platform.

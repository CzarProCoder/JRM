-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS jrm_db;
CREATE USER IF NOT EXISTS 'Julius'@'localhost' IDENTIFIED BY 'Lyonec_2023';
GRANT ALL PRIVILEGES ON `jrm_db`.* TO 'Julius'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'Julius'@'localhost';
FLUSH PRIVILEGES;

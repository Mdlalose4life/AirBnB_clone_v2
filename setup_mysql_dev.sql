--  a script that prepares a MySQL server for the project:
GREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev . * TO 'hbnb_dev'@'localhost';
GRAND SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
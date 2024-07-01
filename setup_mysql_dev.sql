-- Create the database hbnb_dev_db if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user hbnb_dev with password hbnb_dev_pwd if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Revoke all privileges on the database hbnb_dev_db_fake from the hbnb_dev user (just in case this was a typo or error)
REVOKE ALL PRIVILEGES ON hbnb_dev_db_fake.* FROM 'hbnb_dev'@'localhost';

-- Revoke all privileges on the performance_schema database from the hbnb_dev user
REVOKE ALL PRIVILEGES ON performance_schema.* FROM 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush the privileges to ensure that all changes take effect immediately
FLUSH PRIVILEGES;

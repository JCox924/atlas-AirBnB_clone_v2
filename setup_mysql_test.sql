-- Create the database 'hbnb_test_db' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Remove the user 'hbnb_test'@'localhost' if it exists
DROP USER IF EXISTS hbnb_test@localhost;

-- Reload the privileges from the grant tables in the mysql database
FLUSH PRIVILEGES;

-- Create the user 'hbnb_test'@'localhost' with the password 'hbnb_test_pwd' if it does not already exist
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the 'hbnb_test_db' database to the user 'hbnb_test'@'localhost'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privileges on the 'performance_schema' database to the user 'hbnb_test'@'localhost'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Reload the privileges to ensure that all changes take effect immediately
FLUSH PRIVILEGES;

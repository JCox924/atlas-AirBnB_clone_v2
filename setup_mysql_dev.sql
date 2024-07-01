-- Create the database 'hbnb_dev_db' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Drop the user 'hbnb_dev' if it exists, to ensure a clean slate
DROP USER IF EXISTS hbnb_dev@localhost;

-- Refresh the list of privileges to ensure changes take effect
FLUSH PRIVILEGES;

-- Create a new user 'hbnb_dev' with the specified password, if the user doesn't already exist
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the 'hbnb_dev_db' database to the 'hbnb_dev' user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant SELECT privileges on the 'performance_schema' to the 'hbnb_dev' user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

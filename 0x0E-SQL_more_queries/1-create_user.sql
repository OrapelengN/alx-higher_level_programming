-- This script creates the user 'user_0d_1' if it doesn't exist
-- and grants them all privileges on the MySQL server.

-- Drop user if exists (this won't fail if user doesn't exist)
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- Create the user 'user_0d_1' with password 'user_0d_1_pwd'
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables to 'user_0d_1'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the privilege changes
FLUSH PRIVILEGES;

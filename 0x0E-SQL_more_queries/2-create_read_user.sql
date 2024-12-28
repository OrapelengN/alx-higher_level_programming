-- This script creates the database 'hbtn_0d_2' and the user 'user_0d_2' with only SELECT privilege on 'hbtn_0d_2'

-- Create the database 'hbtn_0d_2' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Drop the user 'user_0d_2' if it exists (this won't fail if the user doesn't exist)
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- Create the user 'user_0d_2' with the password 'user_0d_2_pwd'
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege to 'user_0d_2' on the database 'hbtn_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the privilege changes
FLUSH PRIVILEGES;

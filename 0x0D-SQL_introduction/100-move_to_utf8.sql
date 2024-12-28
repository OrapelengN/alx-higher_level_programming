-- Select the database hbtn_0c_0
USE hbtn_0c_0;

-- Convert the database hbtn_0c_0 to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table first_table to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the 'name' column in the table first_table to use utf8mb4_unicode_ci collation (but not explicitly set CHARACTER SET)
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

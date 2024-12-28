-- Create the table 'unique_id' if it doesn't already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,  -- Default value is 1 and the id is unique
    name VARCHAR(256)
);

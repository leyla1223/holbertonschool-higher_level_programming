-- Task: Create the table unique_id with a unique id column
-- This table will have a default value of 1 for id and ensure uniqueness
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

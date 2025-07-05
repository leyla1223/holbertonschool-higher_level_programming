-- Task: Create the table id_not_null with default value 1 for id
-- This query creates the table only if it doesn't already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

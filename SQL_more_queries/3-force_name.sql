-- Task: Create table force_name with non-null name column
-- This query creates the table only if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

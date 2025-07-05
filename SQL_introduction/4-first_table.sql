-- Task: Write a script that creates a table called first_table in the current database in your MySQL server
-- This query creates the table only if it does not already exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

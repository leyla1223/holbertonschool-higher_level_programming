-- Task: List all records from second_table where name contains a value, ordered by score descending
-- This query excludes rows where name is NULL or empty string
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

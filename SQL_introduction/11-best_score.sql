-- Task: List all records with a score >= 10 from second_table showing score and name
-- This query selects score and name where score is 10 or higher, ordered top down
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;

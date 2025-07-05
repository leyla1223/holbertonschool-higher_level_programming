-- Task: List the number of records with the same score in second_table
-- This query groups by score, counts records, and orders by count descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

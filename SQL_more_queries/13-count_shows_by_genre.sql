-- Task: List all genres with number of shows linked (no genres with zero shows)
-- Display genre name as "genre", count as "number_of_shows"
-- Sorted descending by number_of_shows
SELECT g.name AS genre, COUNT(tsg.tv_show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres tsg ON g.id = tsg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;

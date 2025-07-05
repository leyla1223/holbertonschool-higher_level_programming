-- Task: List all shows with their genres; NULL if no genre
-- Sorted by show title asc, genre name asc

SELECT tv_shows.title AS title, genres.name AS name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN genres ON tv_show_genres.genre_id = genres.id
ORDER BY tv_shows.title ASC, genres.name ASC;

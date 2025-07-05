-- Task: List all shows with their genres; NULL if no genre
-- Sorted by show title asc, genre name asc

SELECT
  tv_shows.title,
  tv_genres.name
FROM
  tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY
  tv_shows.title ASC,
  tv_genres.name ASC;

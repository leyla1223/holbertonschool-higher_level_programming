-- Task: List all genres of the show Dexter
-- Display genre names sorted ascending
SELECT g.name
FROM genres g
JOIN tv_show_genres tsg ON g.id = tsg.genre_id
JOIN tv_shows ts ON ts.id = tsg.tv_show_id
WHERE ts.title = 'Dexter'
ORDER BY g.name ASC;

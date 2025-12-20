<<<<<<< HEAD
-- Script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>.
-- First column is called genre.
-- Second column is called number_of_shows.
-- It doesn’t display a genre that doesn’t have any shows linked.
-- Results sort in descending order by the number of shows linked.
-- It uses only one SELECT statement.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
=======
-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
>>>>>>> 7158139 (added new repo)
ORDER BY number_of_shows DESC;

<<<<<<< HEAD
--  This script lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record displays: tv_genres.name - rating sum.
-- It sorts results in descending order by their rating.
-- It uses only one SELECT statement.
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
=======
-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
>>>>>>> 7158139 (added new repo)
GROUP BY tv_genres.name
ORDER BY rating DESC;

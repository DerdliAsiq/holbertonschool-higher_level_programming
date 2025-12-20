<<<<<<< HEAD
-- script lists all shows contained in the database hbtn_0d_tvshows.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id.
-- Results sort in ascending order by tv_shows.title and tv_show_genres.genre_id.
-- If a show doesn’t have a genre, displays NULL.
-- It uses only one SELECT statement.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
=======
-- Lists all shows contained in the database hbtn_0d_tvshows.
-- If a show doesn't have a genre, display NULL.
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
>>>>>>> 7158139 (added new repo)
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

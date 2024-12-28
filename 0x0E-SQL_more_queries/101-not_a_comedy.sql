-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- Only one record where name = Comedy (id can be different) must be contained in the tv_genres table
-- Each record should display: tv_shows.title
-- Sort results in ascending order by the show title
SELECT DISTINCT tv_shows.title FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id AND tv_genres.name = 'Comedy'
WHERE tv_genres.name IS NULL
ORDER BY tv_shows.title ASC;

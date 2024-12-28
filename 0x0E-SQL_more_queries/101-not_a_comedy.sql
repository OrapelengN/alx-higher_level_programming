-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- Only one record where name = Comedy (id can be different) must be contained in the tv_genres table
-- Each record should display: tv_shows.title
-- Sort results in ascending order by the show title
SELECT title
FROM tv_shows
WHERE id NOT IN (
    SELECT show_id
    FROM tv_show_genres
    WHERE genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy')
)
ORDER BY title ASC;

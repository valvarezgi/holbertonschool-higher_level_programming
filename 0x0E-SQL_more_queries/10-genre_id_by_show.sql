--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows, tv_shows_genres
WHERE tv_shows.id = tv_shows_genres.show_id ORDER BY title, genre_id;

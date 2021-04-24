# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (songplay_id int, start_time int, \
                                                                user_id varchar NOT NULL, level int, song_id varchar NOT NULL, artist_id varchar NOT NULL, \
                                                                session_id int, location varchar, user_agent int);")

user_table_create = ("CREATE TABLE IF NOT EXISTS users (user_id varchar NOT NULL, first_name varchar, \
                                                        last_name varchar, gender varchar, level int);")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar, artist_id varchar NOT NULL, \
                                                        year int, duration int);")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists (artist_id varchar NOT NULL, name varchar, location varchar, \
                                                            latitude int, longitude int);")

time_table_create = ("CREATE TABLE IF NOT EXISTS time (start_time int, hour int, day int, week int, \
                                                        month int, year int, weekday int);")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays (songplay_id int, start_time int, \
                                                user_id vachar NOT NULL, level int, song_id varchar NOT NULL, artist_id varchar NOT NULL, \
                                                session_id int, location varchar, user_agent int) \
                                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);")

user_table_insert = ("INSERT INTO users (user_id vachar NOT NULL, first_name varchar, \
                                        last_name varchar, gender varchar, level int) \
                                        VALUES (%s, %s, %s, %s, %s);")

song_table_insert = ("INSERT INTO songs (song_id varchar PRIMARY KEY, title varchar, artist_id varchar NOT NULL, \
                                        year int, duration int) \
                                        VALUES (%s, %s, %s, %s, %s);")

artist_table_insert = ("INSERT INTO artists (artist_id varchar NOT NULL, name varchar, location varchar, \
                                            latitude int, longitude int) \
                                            VALUES (%s, %s, %s, %s, %s,);")

time_table_insert = ("INSERT INTO time (start_time int, hour int, day int, week int, \
                                        month int, year int, weekday int) VALUES (%s, %s, %s, %s, %s, %s, %s);")

# FIND SONGS

song_select = (""" SELECT * FROM songs""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
import repositories.artist_repository as artist_repository
from models.album import Album
from db.run_sql import run_sql

#CREATE
def save(album):
    sql = "INSERT INTO album (artist, arist_id, title, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.artist, album.artist_id, album.title, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

#READ - select all

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        # arist = artist_repository.select(row['artist_id'])
        album = Album(row['artist'], row['title'], row['genre'], row['id'])
        albums.append(album)
    return albums

#READ - select one by id

#DELETE - all
#DELETE - one
#UPDATE
import repositories.artist_repository as artist_repository
from models.album import Album
from db.run_sql import run_sql

#CREATE
def save(album):
    sql = "INSERT INTO albums (artist, arist_id, title, genre) VALUES (%s, %s, %s) RETURNING *"
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
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist_id = result['artist_id']
        artist = artist_repository.select(artist_id)
        album = Album(result['artist'], artist, result['title'], result['genre'], result['id'])
    return album

#DELETE - all
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

#DELETE - one
def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#UPDATE
def update(album):
    sql = "UPDATE albums SET (artist, artist_id, title, genre) = (%s, %s, %s, %s) WHERE id = %s"
    values = [album.artist, album.artist.id, album.title, album.genre, album.id]
    run_sql(sql, values)
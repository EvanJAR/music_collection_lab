import repositories.artist_repository as artist_repository
from models.album import Album
from db.run_sql import run_sql

#CREATE
def save(album):
    sql = "INSERT INTO album (artist, title, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.artist, album.title, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

#READ - select all
#READ - select one by id
#DELETE - all
#DELETE - one
#UPDATE
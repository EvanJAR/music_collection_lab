from models.artist import Artist
from models.album import Album
from db.run_sql import run_sql

def save(artist):
    sql = "INSERT INTO artists (band_name) VALUES (%s) RETURNING id"
    values = [artist.band_name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['band_name'], row['id'])
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['band_name'])
    return artist


def delete_all():
  sql = "DELETE  FROM artists"
  run_sql(sql)

def delete(id):
  sql = "DELETE  FROM artists WHERE id = %s"
  values = [id]
  run_sql(sql, values)
  

def update(artist):
  sql = "UPDATE artist SET (band_name) = (%s) WHERE id = %s"
  values = [artist.band_name, artist.id]
  run_sql(sql, values)
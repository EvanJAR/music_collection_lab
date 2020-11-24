from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository 

album_repository.delete_all()
artist_repository.delete_all()

kurt_k = Artist("Nirvana")
artist_repository.save(kurt_k)


bleach = Album("Nirvana", "Bleach", "alt indie")
album_repository.save()

from typing import List
from app.models.song_model import Song

def obtener_canciones() -> List[Song]:
    canciones = [
        Song(nombre="Canción 1", ruta="/songs/cancion1.mp3"),
        Song(nombre="Canción 2", ruta="/songs/cancion2.mp3"),
        Song(nombre="Canción 3", ruta="/songs/cancion3.mp3"),
    ]
    return canciones

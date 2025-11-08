# src/app/routers/canciones_router.py
from fastapi import APIRouter, HTTPException
from app.database import db
from app.models.song_model import Cancion
from bson import ObjectId

router = APIRouter(prefix="/api/canciones", tags=["Canciones"])

@router.get("/")
def obtener_canciones():
    canciones = list(db["canciones"].find())
    # Convertimos los ObjectId a string para evitar el error JSON
    for c in canciones:
        c["_id"] = str(c["_id"])
    return canciones

# Crear una nueva canción
@router.post("/", response_model=Cancion)
async def crear_cancion(nueva_cancion: Cancion):
    # Convertimos a dict y eliminamos el _id si viene nulo
    cancion_dict = nueva_cancion.dict(by_alias=True)
    cancion_dict.pop("_id", None)  # 👈 esto evita el error DuplicateKeyError

    resultado = db["canciones"].insert_one(cancion_dict)
    cancion_dict["_id"] = str(resultado.inserted_id)
    return cancion_dict
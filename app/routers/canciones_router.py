# src/app/routers/canciones_router.py
import os
import shutil
from typing import List
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.database import db
from app.models.song_model import Cancion
from bson import ObjectId

router = APIRouter(prefix="/api/canciones", tags=["Canciones"])

@router.get("/", response_model=List[Cancion])
def obtener_canciones():
    canciones = list(db["canciones"].find())
    for c in canciones:
        c["_id"] = str(c["_id"])
        # Convertimos la ruta del archivo a URL completa
        c["ruta"] = f"http://127.0.0.1:8000/audio/{c['ruta']}"
    return canciones

@router.post("/upload", response_model=Cancion)
async def subir_cancion(nombre: str, artista: str, archivo: UploadFile = File(...)):
    # Normalizamos el nombre: todo en minúsculas y sin espacios extra
    filename = archivo.filename.lower().replace(" ", "_")

    # Guardar el archivo en la carpeta correcta
    file_path = os.path.join("app/audio_files", filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(archivo.file, buffer)

    # Crear el registro en la base de datos
    cancion_dict = {"nombre": nombre, "artista": artista, "ruta": filename}
    resultado = db["canciones"].insert_one(cancion_dict)
    cancion_dict["_id"] = str(resultado.inserted_id)
    return cancion_dict
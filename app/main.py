# src/app/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import canciones_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="🎵 Music API", version="1.0")
app.mount("/audio", StaticFiles(directory="app/audio_files"), name="audios")

app.include_router(canciones_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # o ["*"] para pruebas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "🎵 API de música funcionando correctamente"}
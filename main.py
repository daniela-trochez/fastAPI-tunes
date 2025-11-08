from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import canciones_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="🎵 API de Canciones")

# Configurar CORS para permitir que Vue (http://localhost:5173) acceda
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringirlo a ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar carpeta de audios
app.mount("/audio", StaticFiles(directory="app/audio_files"), name="audios")

# Incluir router de canciones
app.include_router(canciones_router.router)
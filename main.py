from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import canciones_router

app = FastAPI(title="🎵 API de Canciones")

# Configurar CORS para permitir que Vue (http://localhost:5173) acceda
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringirlo a ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir router
app.include_router(canciones_router.router)

@app.get("/")
def root():
    # Verificamos que la conexión esté disponible
    collections = db.list_collection_names()
    return {
        "message": "Bienvenido a la API de música 🎶",
        "connected_collections": collections
    }
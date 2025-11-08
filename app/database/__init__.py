from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Leer la URI y el nombre de la base
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Conexión al cliente MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]


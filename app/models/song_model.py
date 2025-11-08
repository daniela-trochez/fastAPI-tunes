from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, info=None):  # 👈 aquí agregamos 'info=None'
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        # para Swagger: define que se mostrará como string
        return {"type": "string"}


class Cancion(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    nombre: str
    artista: str
    ruta: str

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True
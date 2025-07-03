from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Mascota(BaseModel):
  nombre: str
  raza: str
  peso: Optional[int]
  genero: str

@app.get("/")
def index():
  return {"mensaje":"creando una API"}

@app.get("/mascotas/{id}")
def mostrar_mascota(id: int):
  return {"data": id}

@app.post("/mascotas")
def insertar_mascota(Mascota: Mascota):
  return {"mensaje": f"Mascota{Mascota.nombre} insertado"}
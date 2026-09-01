from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI(title="API de Cursos", description="API para gestionar cursos", version="1.0.0")

class Curso(BaseModel):
    id: int
    nombre: str
    descripcion: str
    duracion: int
    nivel: str
    
    
@app.get("/")
def home():
    return {"message": "Bienvenido a la API de Cursos"}    
    
    
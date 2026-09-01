from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI(title="API de Cursos", description="API para gestionar cursos", version="1.0.0")

class Curso(BaseModel):
    id: int
    nome: str
    descricao: str
    duracao: int
    nivel: str
    
cursos = []   
    
@app.get("/")
def home():
    return {"message": "Bienvenido a la API de Cursos"}

@app.get("/cursos")
def exibir_cursos(): 
    return cursos

@app.post("/cursos")
def adicionar_cursos(curso: Curso):
       curso.id = len(cursos) + 1
       cursos.append(curso)
       return {"message": "Curso agregado exitosamente", "curso": curso}
   
@app.get("/cursos/{curso_id}")
def obter_curso_por_id(curso_id: int):
    for curso in cursos:
        if curso.id == curso_id:
            return curso
    return {"message": "Curso no encontrado"}

@app.put("/cursos/{curso_id}")
def atualizar_curso(curso_id: int, curso_atualizado: Curso):
    for curso in cursos:
        if curso.id == curso_id:
            curso.nome = curso_atualizado.nome
            curso.descricao = curso_atualizado.descricao
            curso.duracao = curso_atualizado.duracao
            curso.nivel = curso_atualizado.nivel
            return {"message": "Curso actualizado exitosamente", "curso": curso}
    return {"message": "Curso no encontrado"}

@app.delete("/cursos/{curso_id}")
def excluir_curso(curso_id: int):
    for curso in cursos:
        if curso.id == curso_id:
            cursos.remove(curso)
            return {"message": "Curso eliminado exitosamente"}
    return {"message": "Curso no encontrado"}  
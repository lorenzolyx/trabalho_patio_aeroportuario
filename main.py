from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()


app = FastAPI()

class Aeronave(BaseModel):
    matricula: str
    modelo: str
    companhia_aerea: str
    data_chegada: str
    data_saida: str = None

aeronaves = []

@app.post("/aeronaves/", response_model=Aeronave)
def adicionar_aeronave(aeronave: Aeronave):
    aeronaves.append(aeronave)
    return aeronave

@app.get("/aeronaves/")
def listar_aeronaves():
    return aeronaves

@app.put("/aeronaves/{matricula}/", response_model=Aeronave)
def atualizar_aeronave(matricula: str, aeronave: Aeronave):
    for a in aeronaves:
        if a.matricula == matricula:
            a.data_saida = aeronave.data_saida
            return a
    return None

@app.delete("/aeronaves/{matricula}/", response_model=None)
def excluir_aeronave(matricula: str):
    for a in aeronaves:
        if a.matricula == matricula:
            aeronaves.remove(a)
            return None
    return None

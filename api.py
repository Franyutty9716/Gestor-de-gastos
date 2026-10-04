import json
from fastapi import FastAPI
from pydantic import BaseModel

class Gasto(BaseModel):
    descripcion: str
    monto: float
    categoria: str

app = FastAPI()

#Lee los gastos guardados en el archivo; si no existe, devuelve lista vacia
def leer_gastos():
    try:
        with open("gastos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

#Guarda la lista de gastos en el archivo
def guardar_gastos(gastos):
    with open("gastos.json", "w", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, indent=4, ensure_ascii=False)

#Ruta de prueba: responde cuando alguien entra a la direccion principal
@app.get("/")
def inicio():
    return {"mensaje": "API del gestor de gastos funcionando"}

#Devuelve todos los gastos
@app.get("/gastos")
def ver_gastos():
    return leer_gastos()

#Devuelve la suma de todos los montos
@app.get("/total")
def total_gastos():
    total = 0
    for gasto in leer_gastos():
        total += gasto["monto"]
    return {"total": total}

#Recibe un gasto nuevo y lo agrega al archivo
@app.post("/gastos")
def agregar_gasto(gasto: Gasto):
    gastos = leer_gastos()
    gastos.append(gasto.model_dump())
    guardar_gastos(gastos)
    return {"mensaje": "Gasto agregado"}

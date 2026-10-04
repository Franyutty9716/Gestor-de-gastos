import json
from fastapi import FastAPI

app = FastAPI()

#Lee los gastos guardados en el archivo; si no existe, devuelve lista vacia
def leer_gastos():
    try:
        with open("gastos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

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
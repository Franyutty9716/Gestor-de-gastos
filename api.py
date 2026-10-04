from fastapi import FastAPI

app = FastAPI()

#Ruta de prueba: responde cuando alguien entra a la direccion principal
@app.get("/")
def inicio():
    return {"mensaje": "API del gestor de gastos funcionando"}
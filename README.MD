# Gestor de gastos

Programa en Python para registrar y administrar gastos personales desde la consola.

## Qué hace
- Agrega gastos con descripción, monto y categoría
- Muestra la lista de gastos y el total
- Borra gastos
- Guarda los datos en un archivo JSON para no perderlos al cerrar

## Cómo ejecutarlo
1. Instala Python 3
2. Descarga este repositorio
3. En la terminal, dentro de la carpeta, escribe: python gestor_gastos.py

## Tecnologías
- Python
- JSON
- Git y GitHub

## Autor
Angel Franyutty

## Ejecutar la API
   1. Crea y activa un entorno virtual: python -m venv venv y luego venv\Scripts\activate
   2. Instala las librerías: pip install fastapi uvicorn
   3. Enciende la API: uvicorn api:app --reload
   4. Abre http://127.0.0.1:8000/docs para probarla

## Rutas
   - GET /gastos: lista los gastos
   - GET /total: suma de todos los gastos
   - POST /gastos: agrega un gasto
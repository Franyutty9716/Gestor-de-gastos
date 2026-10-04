#Aqui guardo todos los gastos mientras el programa esta abierto
import json
gastos = [] 
def mostrar_menu():
    print("\n--- Gestor de gastos --- ")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Ver total")
    print("4. Borrar gasto")
    print("5. Salir")

#Guardar lista de gastos en un archivo para no perderla al cerrar
def guardar_gastos():
    with open("gastos.json", "w", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, indent=4, ensure_ascii=False)

#Lee el archivo al iniciar; si no existe todavia, empieza con lista vacia
def cargar_gastos():
    try:
        with open("gastos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

#Esta funcion pide los datos del gasto y lo guarda en la lista de gastos
def agregar_gasto():
    descripcion = input("Descripcion: ")
    try:
        monto = float(input("Monto: "))  #Convierte el texto a numero
    except ValueError:
        print("El monto debe ser un numero.")
        return
    categoria = input("Categoria: ")
    gasto = {"descripcion": descripcion, "monto": monto, "categoria": categoria}
    gastos.append(gasto)
    guardar_gastos()
    print("Gasto agregado.")

#Recorre la lista y muestra cada gasto; si esta vacia, avisa y sale con return
def ver_gastos():
    if len(gastos) == 0:  #len() cuenta cuantos elementos hay en lla lista
        print("Aun no hay gastos.")
        return            #return sin nada termina la funcion aqui
    for gasto in gastos:  #"gasto" toma el valor de cada diccionario, uno por uno
        print(f"{gasto['descripcion']} - ${gasto['monto']} ({gasto['categoria']})")

#Suma todos los montos de los gastos y devuelve el resultado
def total_gastos():
    total = 0
    for gasto in gastos:
        total += gasto["monto"] #Suma el monto de cada gasto
    return total    

#Muestra los gastos numerados y borra el que elija el usuario
def borrar_gasto():
    if len(gastos)== 0:
        print("No hay gastos para borrar.")
        return
    for numero, gasto in enumerate(gastos, start=1):
        print(f"{numero}. {gasto['descripcion']} - ${gasto['monto']} ({gasto['categoria']})")
    posicion = int(input("Numero del gasto a borrar: "))
    gasto_borrado = gastos.pop(posicion - 1)
    guardar_gastos()
    print(f"Gasto '{gasto_borrado['descripcion']}' borrado.")

#Al iniciar, cargo los gastos guardados
gastos = cargar_gastos()
        
#Ciclo principal: repite el menu hasta que elija 5 (break)
while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        agregar_gasto()
    elif opcion == "2":
        ver_gastos()
    elif opcion == "3":
        print(f"Total de gastos: ${total_gastos()}")
    elif opcion == "4":
        borrar_gasto()
    elif opcion == "5":
        print("Hasta luego")
        break
    else:
        print("Opcion no valida") 

      
    
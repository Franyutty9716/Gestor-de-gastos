#Aqui guardo todos los gastos mientras el programa esta abierto
gastos = [] 
def mostrar_menu():
    print("\n--- Gestor de gastos --- ")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Ver total")
    print("4. Salir")

#Esta funcion pide los datos del gasto y lo guarda en la lista de gastos
def agregar_gasto():
    descripcion = input("Descripcion: ")
    monto = float(input("Monto: ")) #Convierte el texto a numero
    categoria = input("Categoria: ")
    gasto = {"descripcion": descripcion, "monto": monto, "categoria": categoria}
    gastos.append(gasto)
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

#Ciclo principal: repite el menu hasta que elija 3 (break)
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
        print("Hasta luego")
        break
    else:
        print("Opcion no valida") 


      
    
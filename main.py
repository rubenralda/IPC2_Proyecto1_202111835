from listas import *

listaJugadores = ListaJugadores()
opcion = ""
while opcion != "7":
    print("-----------------------------Menu---------------------------------")
    print("1. Cargar archivo de configuracion")
    print("2. Avanzar jugador")
    print("3. Simular todos los jugadores")
    print("4. Escoger un jugador")
    print("5. Ver pila de premios")
    print("6. Iniciar premiación")
    print("7. Salir")
    opcion = input("Escribe el numero de la opcion:> ")
    match opcion:
        case "1":
            listaJugadores.agregar_jugadores()
        case "7":
            exit()
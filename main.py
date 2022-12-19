from listas import *

listaJugadores = ListaJugadores()
lista_top_10 = ListaTop10()
opcion = ""
while opcion != "8":
    print("-----------------------------Menu---------------------------------")
    print("1. Cargar archivo de configuracion")
    print("2. Avanzar jugador")
    print("3. Simular todos los jugadores")
    print("4. Ver figura del proximo jugador")
    print("5. Ver Top 10 jugadores")
    print("6. Ver pila de premios")
    print("7. Iniciar premiación")
    print("8. Salir")
    opcion = input("Escribe el numero de la opcion:> ")
    match opcion:
        case "1":
            listaJugadores.agregar_jugadores()
            listaJugadores.crearReporte()
        case "2":
            aux = listaJugadores.primero
            listaJugadores.avanzar_jugador()
            lista_top_10.agregar_jugador(aux)
            listaJugadores.crearReporte()
        case "5":
            lista_top_10.imprimirTop10()
        case "8":
            exit()
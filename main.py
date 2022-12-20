from listas import *

lista_jugadores = ListaJugadores()
lista_top10 = ListaTop10()
premios = PilaPremios()
opcion = ""
vacio = False
cargado = False
jugador = None
while opcion != "8":
    print("-----------------------------Menu---------------------------------")
    print("1. Cargar archivo de configuracion")
    print("2. Avanzar jugador en la cola")
    print("3. Simular todos los juegos")
    print("4. Ver figura del proximo jugador")
    print("5. Ver Top 10 jugadores")
    print("6. Ver pila de premios")
    print("7. Dar premio")
    print("8. Salir")
    opcion = input("Escribe el numero de la opcion:> ")
    match opcion:
        case "1":
            lista_jugadores.agregar_jugadores()
            lista_top10.vaciar_lista()
            lista_jugadores.crear_reporte()
            vacio = False
        case "2":
            aux = lista_jugadores.primero
            lista_jugadores.avanzar_jugador()
            lista_top10.agregar_jugador(aux)
            lista_jugadores.crear_reporte()
            if aux == None:
                vacio = True
        case "3":
            aux = lista_jugadores.primero
            while aux != None:
                lista_jugadores.avanzar_jugador()
                lista_top10.agregar_jugador(aux)
                aux = lista_jugadores.primero
            vacio = True
            print("\nLa cola ha sido vaciada.\n")
        case "5":
            print("\n")
            lista_top10.imprimir_top10()
            print("\n")
        case "6":
            premios.agregar_premios()
            premios.crear_reporte()
            cargado = True
        case "7":
            jugador = lista_top10.eliminar_ultimo()
            regalo = premios.eliminar_premio()
            if jugador != None and regalo != None and vacio == True:
                premios.crear_reporte()
                print("Entrega a " + jugador.nombre + " el premio " + regalo.regalo + " por el " + regalo.lugar + " lugar.")
        case "8":
            exit()
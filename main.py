from listas import *
from MatrizDispera import MatrizDispersa

lista_jugadores = ListaJugadores()
lista_top10 = ListaTop10()
premios = PilaPremios()
opcion = ""
vacio = False
cargado = False
jugador = None


def graficar(figura: str):
    matriz = MatrizDispersa(0)
    l = 0
    c = 0
    lineas = figura.split("\n")
    for linea in lineas:
        columnas = linea
        l += 1
        for col in columnas:
            if col != '\n':
                c += 1
                matriz.insert(l, c, col)
        c = 0
    matriz.graficarDibujo('figura')


while opcion != "9":
    print("-----------------------------Menu---------------------------------")
    print("1. Cargar archivo de configuracion")
    print("2. Avanzar jugador en la cola")
    print("3. Simular todos los juegos")
    print("4. Ver figura del proximo jugador")
    print("5. Ver Top 10 jugadores")
    print("6. Cargar pila de premios")
    print("7. Ver pila de premios")
    print("8. Dar premio")
    print("9. Salir")
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
        case "3":
            aux = lista_jugadores.primero
            while aux != None:
                lista_jugadores.avanzar_jugador()
                lista_top10.agregar_jugador(aux)
                aux = lista_jugadores.primero
            print("\nLa cola ha sido vaciada.\n")
        case "4":
            if lista_jugadores.primero == None:
                print("\nNo hay jugadores en la cola\n")
                continue
            graficar(lista_jugadores.primero.puzzle)
            graficar(lista_jugadores.primero.solucion)
        case "5":
            print("\n")
            lista_top10.imprimir_top10()
            print("\n")
        case "6":
            premios.agregar_premios()
            premios.crear_reporte()
            cargado = True
        case "7":
            if cargado == True:
                premios.crear_reporte()
            else:
                print("\n¡No hay pila de premios!\n")
        case "8":
            if lista_jugadores.primero != None:
                print("\nNo hay Top 10 jugadores\n")
                continue
            if cargado == False:
                print("\n¡No hay pila de premios!\n")
                continue
            jugador = lista_top10.eliminar_ultimo()
            if jugador == None:
                continue
            regalo = premios.eliminar_premio()
            if jugador != None and regalo != None:
                premios.crear_reporte()
                print("\nEntrega a " + jugador.nombre + " el premio " +
                      regalo.regalo + " por el " + regalo.lugar + " lugar.\n")
        case "9":
            exit()

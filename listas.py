import xml.etree.ElementTree as eT


class NodoJugador:

    def __init__(self, nombre, edad, movimientos, tamaño, figura, puzzle, solucion):
        self.nombre = nombre
        self.edad = edad
        self.movimientos = movimientos
        self.tamaño = tamaño
        self.figura = figura
        self.puzzle = puzzle
        self.solucion = solucion
        self.punteo = 0
        self.siguiente: NodoJugador = None


class ListaJugadores:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_jugadores(self):
        nombre = edad = movimientos = tamaño = figura = puzzle = solucion = ""
        total_mov = 0
        arbol = eT.parse("entrada.xml")
        jugadores = arbol.findall("./jugador")
        for jugador in jugadores: #recorrer todos los jugadores para guardar
            if total_mov > 10000: #si se paso el limite
                print(
                    "Se llego al limite de movimientos, participantes restantes eliminados.")
                break
            nombre = jugador.find("./datospersonales/nombre").text
            edad = jugador.find("./datospersonales/edad").text
            movimientos = jugador.find("./movimientos").text
            tamaño = jugador.find("./tamaño").text
            if not tamaño.isnumeric(): #si no es un numero entonces no se puede guardar
                print("El tamaño no es correcto " + nombre)
                continue
            if int(tamaño) > 30 or int(tamaño) % 5 != 0: #si cumple con las dimensiones correctas
                print(nombre + " no cumple con los requisitos de la estructura.")
                continue
            figura = jugador.find("./figura").text
            if figura.lower() != "estrella de belen" and figura.lower() != "arbol de navidad" and figura.lower() != "regalo" and figura.lower() != "arbol" and figura.lower() != "estrella" and figura.lower() != "árbol":
                print("La figura " + figura + " no es correcta " + nombre)
                continue
            if not movimientos.isnumeric():
                print("La cantidad de movimientos no es correcta")
                continue
            total_mov += int(movimientos)
            nuevo = NodoJugador(nombre, edad, movimientos,
                                tamaño, figura, puzzle, solucion)
            nuevo.punteo = self.calcular_punteo(int(tamaño), int(movimientos), figura)
            if self.primero == None:
                self.primero = self.ultimo = nuevo
            else:
                self.ultimo.siguiente = nuevo
                self.ultimo = nuevo
            print(self.ultimo.punteo)

    def avanzar_jugador(self):
        if self.primero != None:
            self.primero = self.primero.siguiente

    def calcular_punteo(self,dimension : int, movimientos : int, figura : str):
        punteo = 0
        for i in range(5,35,5):
            punteo += 25
            if dimension == i:
                break
        if movimientos <= 5:
            punteo += 100
        elif movimientos <= 10:
            punteo += 75
        elif movimientos <= 15:
            punteo += 50
        elif movimientos <= 20:
            punteo += 25
        if figura.lower() == "estrella de belen" or figura.lower() == "estrella":
            punteo += 500
        elif figura.lower() == "arbol de navidad" or figura.lower() == "arbol":
            punteo += 250
        elif figura.lower() == "regalo":
            punteo += 100
        return punteo

class ListaTop10:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_jugador(self, jugador: NodoJugador):
        if self.primero == None:
            self.primero = self.ultimo = jugador
        else:
            aux = self.primero
            for i in range(1,10):
                if jugador.punteo <= aux.punteo:
                    aux.siguiente = jugador
                    aux.siguiente.siguiente = aux.siguiente
                    print("El " + self.ultimo.nombre + " es el Top" + str(i))
                    break
                
                aux = aux.siguiente
                if aux == None:
                    break

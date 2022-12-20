import xml.etree.ElementTree as eT
import os
import webbrowser


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
        self.anterior: NodoJugador = None


class ListaJugadores:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_jugadores(self):
        nombre = edad = movimientos = tamaño = figura = puzzle = solucion = ""
        self.primero = self.ultimo = None
        total_mov = 0
        arbol = eT.parse("entrada.xml")
        jugadores = arbol.findall("./jugador")
        for jugador in jugadores:  # recorrer todos los jugadores para guardar
            if total_mov > 10000:  # si se paso el limite
                print(
                    "\nAdvertencia: Se llego al limite de movimientos, participantes restantes eliminados.\n")
                break
            nombre = jugador.find("./datospersonales/nombre").text
            edad = jugador.find("./datospersonales/edad").text
            movimientos = jugador.find("./movimientos").text
            tamaño = jugador.find("./tamaño").text
            if not tamaño.isnumeric():  # si no es un numero entonces no se puede guardar
                print("\nError: el tamaño no es correcto " + nombre + "\n")
                continue
            # si cumple con las dimensiones correctas
            if int(tamaño) > 30 or int(tamaño) % 5 != 0:
                print("\nAdvertencia: " + nombre +
                      " no cumple con los requisitos de la estructura, jugador no agregado.\n")
                continue
            figura = jugador.find("./figura").text
            if figura.lower() != "estrella de belen" and figura.lower() != "arbol de navidad" and figura.lower() != "regalo" and figura.lower() != "arbol" and figura.lower() != "estrella" and figura.lower() != "árbol":
                print("\nAdvertencia: La figura " + figura +
                      " no existe " + nombre + ", jugador no agregado.\n")
                continue
            if not movimientos.isnumeric():
                print("\nError: La cantidad de movimientos no es correcta.\n")
                continue
            total_mov += int(movimientos)
            nuevo = NodoJugador(nombre, edad, movimientos,
                                tamaño, figura, puzzle, solucion)
            nuevo.punteo = self.calcular_punteo(
                int(tamaño), int(movimientos), figura)
            if self.primero == None:
                self.primero = self.ultimo = nuevo
            else:
                self.ultimo.siguiente = nuevo
                self.ultimo = nuevo

    def avanzar_jugador(self):
        if self.primero != None:
            print("\n¡El " + self.primero.nombre +
                  " jugador termino de jugar!\n")
            self.primero = self.primero.siguiente
        else:
            print("\nAdvertencia: La cola esta vacia.\n")

    def calcular_punteo(self, dimension: int, movimientos: int, figura: str):
        punteo = 0
        for i in range(5, 35, 5):
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

    def report(self):
        if self.primero == None:
            return ""
        aux = self.primero
        conexion = ""
        text = ""
        text += "rankdir=LR; \n "
        text += "node[shape=component, style=filled, color=skyBlue, fontname=\"Century Gothic\"]; \n "
        text += "graph [fontname=\"Century Gothic\"]; \n "
        text += "labelloc=\"t\"; label=\"Cola de jugadores\"; \n"
        while True:
            text += aux.nombre + str(aux.edad) + "[label=\"Nombre: " + aux.nombre + "\\nEdad: " + \
                aux.edad+"\\nMovimientos: " + str(aux.movimientos)+"\\nTamaño: " + \
                str(aux.tamaño) + "\\nFigura: " + aux.figura + \
                "\\nPunteo: " + str(aux.punteo) + "\"]\n"
            conexion += aux.nombre + str(aux.edad)
            aux = aux.siguiente
            if aux == None:
                break
            conexion += " -> "
        text += conexion
        return text

    def crear_reporte(self):
        contenido = "digraph G{\n\n"
        r = open("./textos/colaJugadores.txt", "w")
        contenido += str(self.report())
        contenido += "\n}"
        r.write(contenido)
        r.close()
        if self.primero != None:
            os.system(
                "dot -Tpng -Gcharset=latin1 textos/colaJugadores.txt -o colaJugadores.png")
            webbrowser.open("colaJugadores.png")


class ListaTop10:

    def __init__(self):
        self.conteo = 0
        self.primero = None
        self.ultimo = None

    def agregar_jugador(self, nuevo: NodoJugador):
        if nuevo == None:
            print("La cola esta vacia.")
            return
        nuevo.siguiente = None
        if self.ultimo == None:
            self.primero = self.ultimo = nuevo
            self.conteo += 1
        else:
            aux = self.primero
            if nuevo.punteo > self.primero.punteo:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
                self.conteo += 1
                if self.conteo > 10:
                    self.ultimo = self.ultimo.anterior
                    self.ultimo.siguiente = None
                    self.conteo = 10
                return
            while True:
                if nuevo.punteo <= aux.punteo:
                    if aux.siguiente == None:
                        aux.siguiente = nuevo
                        self.ultimo = nuevo
                        self.ultimo.anterior = aux
                        self.conteo += 1
                        if self.conteo > 10:
                            self.ultimo = self.ultimo.anterior
                            self.ultimo.siguiente = None
                            self.conteo = 10
                        break
                    elif nuevo.punteo >= aux.siguiente.punteo:
                        nuevo.siguiente = aux.siguiente
                        aux.siguiente.anterior = nuevo
                        nuevo.anterior = aux
                        aux.siguiente = nuevo
                        self.conteo += 1
                        if self.conteo > 10:
                            self.ultimo = self.ultimo.anterior
                            self.ultimo.siguiente = None
                            self.conteo = 10
                        break
                    aux = aux.siguiente

    def imprimir_top10(self):
        if self.ultimo != None:
            aux = self.primero
        else:
            aux = None
        for i in range(1, 11):
            if aux != None:
                print(str(i) + ". " + aux.nombre +
                      " Punteo: " + str(aux.punteo))
                aux = aux.siguiente
            else:
                print(str(i) + ".")

    def vaciar_lista(self):
        self.conteo = 0
        self.primero = None
        self.ultimo = None
    
    def eliminar_ultimo(self):
        if self.ultimo == None:
            print("No hay Top 10")
            return None
        if self.ultimo.anterior != None:
            self.ultimo = self.ultimo.anterior
            aux = self.ultimo.siguiente
            self.ultimo.siguiente = None
            self.conteo -= 1
            return aux
        else:
            self.conteo = 0
            self.ultimo = None
            print("Ultimo premio entregado")
            return self.primero


class Premios:

    def __init__(self, lugar, regalo) -> None:
        self.lugar = lugar
        self.regalo = regalo
        self.siguiente: Premios = None
        self.anterior: Premios = None


class PilaPremios:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_premios(self):
        self.primero = self.ultimo = None
        arbol = eT.parse("premios.xml")
        premios = arbol.findall("./premio")
        for premio in premios:  # recorrer todos los premios para guardar
            lugar = premio.find("./lugar").text
            regalo = premio.find("./regalo").text
            nuevo = Premios(lugar, regalo)
            if self.ultimo == None:
                self.primero = self.ultimo = nuevo
            else:
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo

    def report(self):
        if self.ultimo == None:
            return ""
        aux = self.primero
        conexion = ""
        text = ""
        text += "rankdir=TB; \n "
        text += "node[shape=cds, style=filled, color=pink, fontname=\"Century Gothic\"]; \n "
        text += "graph [fontname=\"Century Gothic\"]; \n "
        text += "labelloc=\"t\"; label=\"Pila de premios\"; \n"
        while True:
            text += aux.lugar + "[label=\"Lugar: " + \
                aux.lugar + "\\nPremio: " + aux.regalo + "\"]\n"
            conexion += aux.lugar
            aux = aux.siguiente
            if aux == None:
                break
            conexion += " -> "
        text += conexion
        return text

    def crear_reporte(self):
        contenido = "digraph G{\n\n"
        r = open("./textos/pilaPremios.txt", "w")
        contenido += str(self.report())
        contenido += "\n}"
        r.write(contenido)
        r.close()
        if self.primero != None:
            os.system(
                "dot -Tpng -Gcharset=latin1 textos/pilaPremios.txt -o pilaPremios.png")
            webbrowser.open("pilaPremios.png")

    def eliminar_premio(self):
        if self.ultimo == None:
            return None
        else:
            if self.primero.siguiente == None:
                self.ultimo = None
                return self.primero 
            self.primero = self.primero.siguiente
            aux = self.primero.anterior
            return aux
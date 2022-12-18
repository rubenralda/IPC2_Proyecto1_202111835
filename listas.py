class NodoJugador:

    def __init__(self,nombre,edad,movimientos,tamaño,figura,puzzle,solucion):
        self.nombre=nombre
        self.edad=edad
        self.movimientos=movimientos
        self.tamaño=tamaño
        self.figura=figura
        self.puzzle=puzzle
        self.solucion=solucion
        self.siguiente=None

class ListaJugadores:

    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def agregarJugador(self,nombre,edad,movimientos,tamaño,figura,puzzle,solucion):
        nuevo = NodoJugador(nombre,edad,movimientos,tamaño,figura,puzzle,solucion)
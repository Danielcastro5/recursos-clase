# Lab 2 B
# Nombre:Daniel esteban castro calderin 
# Grupo: 32
# Cod Estudiante:202310422

######################################
#                                    #
#             Punto #1               #
#                                    #
######################################

# Cree un método llamado sumaImpares(...) dentro de la clase Lista Simplemente Enlazada (LSL) que sume los datos que son impares y retorne el valor de la suma, incluya todo el código de la declaración de la clase LSL y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class LSL:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def sumaImpares(self):
        suma = 0
        actual = self.cabeza
        while actual:
            if actual.dato % 2 != 0:
                suma += actual.dato
            actual = actual.siguiente
        return suma

lista = LSL()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)

print(lista.sumaImpares())
# FIN_SOLUCION

######################################
#                                    #
#             Punto #2               #
#                                    #
######################################

# Implemente un método llamado rotarDerecha(...) dentro de la clase Lista Simplemente Enlazada (LSL) que rote los elementos de la lista una posición a la derecha. Incluya todo el código de la declaración de la clase LSL y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class LSL:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def rotarDerecha(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return

        ultimo = self.cabeza
        while ultimo.siguiente.siguiente:
            ultimo = ultimo.siguiente

        nuevo_cabeza = ultimo.siguiente
        ultimo.siguiente = None
        nuevo_cabeza.siguiente = self.cabeza
        self.cabeza = nuevo_cabeza

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

lista = LSL()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)

print("Lista original:")
lista.imprimir()
lista.rotarDerecha()

print("Lista después de rotar a la derecha:")
lista.imprimir()
# FIN_SOLUCION


######################################
#                                    #
#             Punto #3               #
#                                    #
######################################

# Considerando que solo tiene listas ordenadas ascendentemente, desarrolle un método llamado fusionarListaOrdenada(...) dentro de la clase Lista Simplemente Enlazada (LSL) que reciba una lista simplemente enlazada ordenada y la fusione de manera ordenada con la lista sobre la cual se llama el método. Incluya todo el código de la declaración de la clase LSL y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class LSL:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def fusionarListaOrdenada(self, lista_ordenada):
        if lista_ordenada.cabeza is None:
            return

        actual_self = self.cabeza
        actual_lista_ordenada = lista_ordenada.cabeza

        if actual_self is None:
            self.cabeza = actual_lista_ordenada
            return

        if actual_self.dato > actual_lista_ordenada.dato:
            nuevo_cabeza = actual_lista_ordenada
            nuevo_cabeza.siguiente = self.cabeza
            self.cabeza = nuevo_cabeza
            actual_lista_ordenada = actual_lista_ordenada.siguiente

        while actual_self.siguiente and actual_lista_ordenada:
            if actual_self.siguiente.dato > actual_lista_ordenada.dato:
                nuevo_nodo = actual_lista_ordenada
                nuevo_nodo.siguiente = actual_self.siguiente
                actual_self.siguiente = nuevo_nodo
                actual_lista_ordenada = actual_lista_ordenada.siguiente
            actual_self = actual_self.siguiente

        if actual_lista_ordenada:
            actual_self.siguiente = actual_lista_ordenada

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

lista1 = LSL()
lista1.agregar(1)
lista1.agregar(3)
lista1.agregar(5)

lista2 = LSL()
lista2.agregar(2)
lista2.agregar(4)
lista2.agregar(6)

print("Lista 1 original:")
lista1.imprimir()

print("Lista 2 original:")
lista2.imprimir()

lista1.fusionarListaOrdenada(lista2)

print("Lista 1 después de fusionar:")
lista1.imprimir()
# FIN_SOLUCION

######################################
#                                    #
#             Punto #4               #
#                                    #
######################################

# Cree un método llamado eliminarDesde(...) dentro de la clase Lista Simplemente Enlazada (LSL) que reciba un índice n como parámetro y elimine todos los nodos a partir del n-ésimo elemento desde el principio de la lista. Incluya todo el código de la declaración de la clase LSL y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class LSL:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminarDesde(self, n):
        if n == 0:
            self.cabeza = None
            return

        actual = self.cabeza
        for _ in range(n - 1):
            if actual.siguiente is None:
                return
            actual = actual.siguiente

        actual.siguiente = None

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

lista = LSL()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)

print("Lista original:")
lista.imprimir()

lista.eliminarDesde(3)

print("Lista después de eliminar desde el índice 3:")
lista.imprimir()
# FIN_SOLUCION


######################################
#                                    #
#             Punto #5               #
#                                    #
######################################

# Cree un método llamado intercambiarMayorMenor(...) dentro de la clase Lista Simplemente Enlazada (LSL) que intercambie la posición de los nodos que contienen el dato mayor y el menor de la lista. Incluya todo el código de la declaración de la clase LSL y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class LSL:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def intercambiarMayorMenor(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return

        mayor = self.cabeza
        menor = self.cabeza

        actual = self.cabeza
        while actual:
            if actual.dato > mayor.dato:
                mayor = actual
            elif actual.dato < menor.dato:
                menor = actual
            actual = actual.siguiente

        temp = mayor.dato
        mayor.dato = menor.dato
        menor.dato = temp

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

lista = LSL()
lista.agregar(5)
lista.agregar(2)
lista.agregar(8)
lista.agregar(1)
lista.agregar(9)

print("Lista original:")
lista.imprimir()

lista.intercambiarMayorMenor()

print("Lista después de intercambiar mayor y menor:")
lista.imprimir()
# FIN_SOLUCION

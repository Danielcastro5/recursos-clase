# Lab 5 B
# Nombre:Daniel esteban castro 
# Grupo: 32
# Cod Estudiante:202310422

######################################
#                                    #
#             Punto #1               #
#                                    #
######################################

# Escriba una función recursiva llamada `suma_digitos(n)` que reciba un número entero `n` y retorne la suma de sus dígitos. Por ejemplo, `suma_digitos(123)` debería retornar `6`.

# INICIO_SOLUCION
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
# FIN_SOLUCION

######################################
#                                    #
#             Punto #2               #
#                                    #
######################################

# Escriba una función recursiva llamada `es_palindromo(lista)` que reciba una lista doblemente enlazada donde el dato de cada nodo es una letra, y determine si el texto conformado por las letras de la lista es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda). La función debe retornar True si es un palíndromo y False en caso contrario. Por ejemplo, llamar la función `es_palindromo` con una lista con el contenido "radar" o con el contenido "como la ruta nos aporto otro paso natural" debería retornar `True`. Incluya el código de la declaración de la clase Lista Doblemente Enlazada (LDL) junto con los métodos que considere necesarios.


# INICIO_SOLUCIO
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class LDL:
    def __init__(self):
        self.cabecera = None
        self.cola = None

    def agregar_al_final(self, dato):
        nodo = Nodo(dato)
        if self.cabecera is None:
            self.cabecera = nodo
            self.cola = nodo
        else:
            self.cola.siguiente = nodo
            nodo.anterior = self.cola
            self.cola = nodo

    def es_palindromo(self):
        def comparar(nodo1, nodo2):
            if nodo1 is None and nodo2 is None:
                return True
            if nodo1 is None or nodo2 is None:
                return False
            if nodo1.dato != nodo2.dato:
                return False
            return comparar(nodo1.siguiente, nodo2.anterior)

        return comparar(self.cabecera, self.cola)
ldl = LDL()
ldl.agregar_al_final('r')
ldl.agregar_al_final('a')
ldl.agregar_al_final('d')
ldl.agregar_al_final('a')
ldl.agregar_al_final('r')

print(ldl.es_palindromo())
# FIN_SOLUCION

######################################
#                                    #
#             Punto #3               #
#                                    #
######################################

# Escriba una función recursiva llamada `maximo(lista)` que reciba una lista de números y retorne el valor máximo en la lista. Por ejemplo, `maximo([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])` debería retornar `9`.

# INICIO_SOLUCION
def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_resto = maximo(lista[1:])
        return lista[0] if lista[0] > max_resto else max_resto

print(maximo([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) 
# FIN_SOLUCION

######################################
#                                    #
#             Punto #4               #
#                                    #
######################################

# Escriba una función recursiva llamada `contar_ocurrencias(lista_enlazada)` que reciba una lista simplemente enlazada y retorne en un HashMap cuántas veces aparece cada elemento en la lista. Por ejemplo, si tiene una lista simplemente enlazada con los elementos ["casa", "patio", "mansion", "casa", "mansion", "mansion"], al llamar la función `contar_ocurrencias` debería retornar un HashMap con los elementos "casa" -> 2, "patio" -> 1, mansión -> 2. Incluya el código de la declaración de la clase Lista Simplemente Ligada (LSL), la clase HashMap (HM), los nodos para estas estructuras y los métodos que considere necesarios.

# INICIO_SOLUCION
class NodoLSL:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class LSL:
    def __init__(self):
        self.cabecera = None

    def agregar_al_final(self, dato):
        nodo = NodoLSL(dato)
        if self.cabecera is None:
            self.cabecera = nodo
        else:
            actual = self.cabecera
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

class HashMap:
    def __init__(self):
        self.mapa = {}

    def agregar(self, clave, valor):
        self.mapa[clave] = valor

    def actualizar(self, clave, valor):
        if clave in self.mapa:
            self.mapa[clave] = valor

    def obtener(self, clave):
        return self.mapa.get(clave, 0)

def contar_ocurrencias(lista_enlazada):
    hashmap = HashMap()
    actual = lista_enlazada.cabecera

    def recursiva(nodo):
        if nodo is None:
            return
        contar = hashmap.obtener(nodo.dato)
        hashmap.actualizar(nodo.dato, contar + 1)
        recursiva(nodo.siguiente)

    recursiva(actual)
    return hashmap.mapa
  
lsa = LSL()
lsa.agregar_al_final("casa")
lsa.agregar_al_final("patio")
lsa.agregar_al_final("mansion")
lsa.agregar_al_final("casa")
lsa.agregar_al_final("mansion")
lsa.agregar_al_final("mansion")

print(contar_ocurrencias(lsa))
Salida: {'casa': 2, 'patio': 1, 'mansion': 3}
# FIN_SOLUCION

######################################
#                                    #
#             Punto #5               #
#                                    #
######################################

# Escriba un método recursivo dentro de la clase Lista Simplemente Ligada(LSL) llamado `invertir_lista()` que invierta la lista, el método no retornará nada pero los elementos deben quedar invertidos una vez se recorra la lista después de llamar el método. Incluya el código de la declaración de la clase Lista Simplemente Ligada (LSL), la clase NodoSimple (NS) y los métodos que considere necesarios.


# INICIO_SOLUCION
class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class LSL:
    def __init__(self):
        self.cabecera = None

    def agregar_al_final(self, dato):
        nodo = NodoSimple(dato)
        if self.cabecera is None:
            self.cabecera = nodo
        else:
            actual = self.cabecera
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def imprimir_lista(self):
        actual = self.cabecera
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def invertir_lista(self):
        self.cabecera = self._invertir_lista(self.cabecera)

    def _invertir_lista(self, nodo):
        if nodo is None or nodo.siguiente is None:
            return nodo
        nuevo_cabecera = self._invertir_lista(nodo.siguiente)
        nodo.siguiente.siguiente = nodo
        nodo.siguiente = None
        return nuevo_cabecera

lsa = LSL()
lsa.agregar_al_final("A")
lsa.agregar_al_final("B")
lsa.agregar_al_final("C")
lsa.agregar_al_final("D")
lsa.agregar_al_final("E")

print("Lista original:")
lsa.imprimir_lista()

lsa.invertir_lista()

print("Lista invertida:")
lsa.imprimir_lista()
# FIN_SOLUCION

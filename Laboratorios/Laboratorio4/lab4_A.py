# Lab 3 A
# Nombre: Daniel Calderin
# Grupo: 32
# Cod Estudiante: 202310422

######################################
#                                    #
#             Punto #1               #
#                                    #
######################################

# Partiendo de la clase HashMap, elimine el atributo "conteo" y en su lugar cree un método llamado contar(...), este método contará todos los pares clave valor existentes en el HashMap, y retornará el valor. Incluya todo el código de la declaración de las clases HashMap (HM), NodoMapeo (NM) y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class NodoMapeo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class HashMap:
    def __init__(self):
        self.tamaño = 10
        self.tabla = [None] * self.tamaño

    def agregar(self, clave, valor):
        indice = hash(clave) % self.tamaño
        if self.tabla[indice] is None:
            self.tabla[indice] = NodoMapeo(clave, valor)
        else:
            actual = self.tabla[indice]
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = NodoMapeo(clave, valor)

    def contar(self):
        conteo = 0
        for nodo in self.tabla:
            while nodo:
                conteo += 1
                nodo = nodo.siguiente
        return conteo

hm = HashMap()
hm.agregar("clave1", "valor1")
hm.agregar("clave2", "valor2")
hm.agregar("clave3", "valor3")

print(hm.contar())  
# FIN_SOLUCION

######################################
#                                    #
#             Punto #2               #
#                                    #
######################################


# Cree una clase llamada 'Cancionero', el cual tendrá un atributo llamado 'canciones' que será un HashMap, las llaves serán nombres de un artistas y como valor un diccionario, dicho diccionario a su vez tendrá como llave el nombre de una canción del artista y como valor las letras o liricas de la canción. Dentro de la clase cancionero cree el método 'ingresarCanción(...)' que reciba el nombre de un artista  y de una canción de dicho artista y lo almacene dentro de la estructura cancionero si las liricas existen, de lo contrario no. También cree un método llamado 'obtenerCancion(...)' que recibirá el nombre de un artista y una canción y retornará la canción si existe. Por último implemente un método llamado mostrarCancionesArtista() que recibe el nombre de un artista e imprime todas las canciones con las líricas que se encuentran almacenadas para ese artista. Puede consultar las liricas a través la API https://api.lyrics.ovh/v1/{artista}/{cancion} donde debe reemplazar {artista} y {cancion} por los valores correspondientes. Si tiene dudas siga las instrucciones de la guia de autoestudio: https://comunidadiushedu.sharepoint.com/:w:/s/DS202402-CursoEstructurasdeDatos/ETIYUsYg0w9KjeidLGL0J_wBoV0UlkNOkctYA36W8-Ezrg?e=rhfqH3


# INICIO_SOLUCION
import requests

class Cancionero:
    def __init__(self):
        self.canciones = {}

    def ingresarCancion(self, artista, cancion):
        if artista not in self.canciones:
            self.canciones[artista] = {}
        url = f"(link unavailable)"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            liricas = respuesta.json()["lyrics"]
            self.canciones[artista][cancion] = liricas

    def obtenerCancion(self, artista, cancion):
        if artista in self.canciones and cancion in self.canciones[artista]:
            return self.canciones[artista][cancion]
        return None

    def mostrarCancionesArtista(self, artista):
        if artista in self.canciones:
            for cancion, liricas in self.canciones[artista].items():
                print(f"Canción: {cancion}")
                print(f"Líricas:\n{liricas}\n")

cancionero = Cancionero()
cancionero.ingresarCancion("Queen", "Bohemian Rhapsody")
cancionero.ingresarCancion("Queen", "We Will Rock You")
cancionero.mostrarCancionesArtista("Queen")
print(cancionero.obtenerCancion("Queen", "Bohemian Rhapsody"))
# FIN_SOLUCION

######################################
#                                    #
#             Punto #3               #
#                                    #
######################################

# Añada un método llamado eliminar_clave(...) en la clase HashMap que reciba una clave como parámetro y elimine el par clave-valor asociado a esa clave del HashMap, si existe. Incluya todo el código de la declaración de las clases HashMap (HM), NodoMapeo (NM) y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class NodoMapeo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class HashMap:
    def __init__(self):
        self.tamaño = 10
        self.tabla = [None] * self.tamaño

    def agregar(self, clave, valor):
        indice = hash(clave) % self.tamaño
        if self.tabla[indice] is None:
            self.tabla[indice] = NodoMapeo(clave, valor)
        else:
            actual = self.tabla[indice]
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = NodoMapeo(clave, valor)

    def eliminar_clave(self, clave):
        indice = hash(clave) % self.tamaño
        if self.tabla[indice] is None:
            return
        if self.tabla[indice].clave == clave:
            self.tabla[indice] = self.tabla[indice].siguiente
            return
        actual = self.tabla[indice]
        while actual.siguiente:
            if actual.siguiente.clave == clave:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

hm = HashMap()
hm.agregar("clave1", "valor1")
hm.agregar("clave2", "valor2")
hm.agregar("clave3", "valor3")

hm.eliminar_clave("clave2")
# FIN_SOLUCION

######################################
#                                    #
#             Punto #4               #
#                                    #
######################################

# Implemente un método llamado fusionar(...) en la clase HashMap que reciba como parámetro otro objeto HashMap y fusione los pares clave-valor de este último en el HashMap actual, sobrescribiendo los valores en caso de claves duplicadas. Incluya todo el código de la declaración de las clases HashMap (HM), NodoMapeo (NM) y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class NodoMapeo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class HashMap:
    def __init__(self):
        self.tamaño = 10
        self.tabla = [None] * self.tamaño

    def agregar(self, clave, valor):
        indice = hash(clave) % self.tamaño
        if self.tabla[indice] is None:
            self.tabla[indice] = NodoMapeo(clave, valor)
        else:
            actual = self.tabla[indice]
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = NodoMapeo(clave, valor)

    def fusionar(self, otro_mapa):
        for nodo in otro_mapa.tabla:
            while nodo:
                self.agregar(nodo.clave, nodo.valor)
                nodo = nodo.siguiente

hm1 = HashMap()
hm1.agregar("clave1", "valor1")
hm1.agregar("clave2", "valor2")

hm2 = HashMap()
hm2.agregar("clave2", "nuevo_valor2")
hm2.agregar("clave3", "valor3")

hm1.fusionar(hm2)
# FIN_SOLUCION

######################################
#                                    #
#             Punto #5               #
#                                    #
######################################

# Implemente un método llamado clonar(...) en la clase HashMap que devuelva una nueva instancia de HashMap con los mismos pares clave-valor que el HashMap original. Incluya todo el código de la declaración de las clases HashMap (HM), NodoMapeo (NM) y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class NodoMapeo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class HashMap:
    def __init__(self):
        self.tamaño = 10
        self.tabla = [None] * self.tamaño

    def agregar(self, clave, valor):
        indice = hash(clave) % self.tamaño
        if self.tabla[indice] is None:
            self.tabla[indice] = NodoMapeo(clave, valor)
        else:
            actual = self.tabla[indice]
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = NodoMapeo(clave, valor)

    def clonar(self):
        nuevo_mapa = HashMap()
        for nodo in self.tabla:
            while nodo:
                nuevo_mapa.agregar(nodo.clave, nodo.valor)
                nodo = nodo.siguiente
        return nuevo_mapa

hm = HashMap()
hm.agregar("clave1", "valor1")
hm.agregar("clave2", "valor2")

hm_clonado = hm.clonar()
# FIN_SOLUCION

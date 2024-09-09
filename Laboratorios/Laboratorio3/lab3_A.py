# Lab 3 A
# Nombre:Daniel Calderin
# Grupo: 32
# Cod Estudiante:202310422

######################################
#                                    #
#             Punto #1               #
#                                    #
######################################

# Cree un método llamado partir(...) dentro de la clase Cola que reciba un parámetro 'n', desencole 'n' elementos y retorne una nueva cola con los elementos que fueron desencolados. Incluya todo el código de la declaración de las clase Cola y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos.pop(0)

    def partir(self, n):
        nueva_cola = Cola()
        for _ in range(n):
            elemento = self.desencolar()
            if elemento is not None:
                nueva_cola.encolar(elemento)
        return nueva_cola

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)

cola_partida = cola.partir(3)
print(cola_partida.elementos)  # [1, 2, 3]
print(cola.elementos)  # [4, 5]
# FIN_SOLUCION

######################################
#                                    #
#             Punto #2               #
#                                    #
######################################

# Cree un método llamado encolaAlPrincipio(...) dentro de la clase Cola que reciba un dato y lo encole al inicio de la lista de tal forma que sea el siguiente elemento que va a salir al desencolar. Incluya todo el código de la declaración de la clase Cola y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos.pop(0)

    def encolaAlPrincipio(self, elemento):
        self.elementos.insert(0, elemento)

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

cola.encolaAlPrincipio(0)

print(cola.desencolar())  # 0
print(cola.desencolar())  # 1
print(cola.desencolar())  # 2
print(cola.desencolar())  # 3
# FIN_SOLUCION


######################################
#                                    #
#             Punto #3               #
#                                    #
######################################

# Realice los cambios requeridos a la clase NodoPrioridad y al método encolar(...) de la clase ColaPrioridad de tal forma que las prioridades en los nodos puedan ser las siguientes: "CRITICAL", "URGENT", "PRIORITY", "NORMAL", "IRRELEVANT" (en ese orden). Incluya todo el código de la declaración de las clases NodoPrioridad, ColaPrioridad y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class NodoPrioridad:
    def __init__(self, valor, prioridad):
        self.valor = valor
        self.prioridad = prioridad

class ColaPrioridad:
    def __init__(self):
        self.elementos = []

    def encolar(self, valor, prioridad):
        prioridades = {"CRITICAL": 5, "URGENT": 4, "PRIORITY": 3, "NORMAL": 2, "IRRELEVANT": 1}
        nodo = NodoPrioridad(valor, prioridades[prioridad])
        self.elementos.append(nodo)
        self.elementos.sort(key=lambda x: x.prioridad, reverse=True)

    def desencolar(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos.pop(0).valor

cola = ColaPrioridad()
cola.encolar("Tarea 1", "NORMAL")
cola.encolar("Tarea 2", "URGENT")
cola.encolar("Tarea 3", "CRITICAL")

print(cola.desencolar())  # Tarea 3
print(cola.desencolar())  # Tarea 2
print(cola.desencolar())  # Tarea 1
# FIN_SOLUCION

######################################
#                                    #
#             Punto #4               #
#                                    #
######################################

# Cree una función llamada main donde simule una aplicación básica de compras y despacho de productos. 
# - Al iniciar el programa deberá pedirle al usuario que seleccione una de las siguientes opciones:
#   - Comprar producto: Si el usuario selecciona esta opción se le dará la oportunidad de ingresar su nombre y un producto a comprar. Esta info se debe agregar a la cola
#   - Validar siguiente producto: mostrará la info del siguiente  nombre y el producto a despachar sin desencolarlo.
#   - Despachar producto: Si el usuario selecciona esta opción se desencolará un elemento y se mostrará la info del nombre y el producto a despachar.
#   - Salir del programa: Sale del programa

# INICIO_SOLUCION
from cola import Cola

def main():
    cola_compras = Cola()

    while True:
        print("Seleccione una opción:")
        print("1. Comprar producto")
        print("2. Validar siguiente producto")
        print("3. Despachar producto")
        print("4. Salir del programa")

        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            producto = input("Ingrese el producto a comprar: ")
            cola_compras.encolar((nombre, producto))
        elif opcion == "2":
            if not cola_compras.está_vacia():
                nombre, producto = cola_compras.primer_elemento()
                print(f"Nombre: {nombre}, Producto: {producto}")
            else:
                print("No hay productos en la cola")
        elif opcion == "3":
            if not cola_compras.está_vacia():
                nombre, producto = cola_compras.desencolar()
                print(f"Nombre: {nombre}, Producto: {producto}")
            else:
                print("No hay productos en la cola")
        elif opcion == "4":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
# FIN_SOLUCION


######################################
#                                    #
#             Punto #5               #
#                                    #
######################################

# Cree un método llamado invertirPila(...) dentro de la clase Pila que invierta el orden de los elementos en la pila. Incluya todo el código de la declaración de la clase Pila y un ejemplo del funcionamiento del método.

# INICIO_SOLUCION
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos.pop()

    def invertirPila(self):
        self.elementos = self.elementos[::-1]

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print(pila.elementos)  # [1, 2, 3]

pila.invertirPila()

print(pila.elementos)  # [3, 2, 1]
# FIN_SOLUCION
